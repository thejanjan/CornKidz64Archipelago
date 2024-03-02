import math
from typing import Dict, Any, Set
from BaseClasses import Region, Entrance, Location, Item, ItemClassification, CollectionState
from worlds.AutoWorld import World
from .Items import item_table, get_trap_items, get_filler_items, CK64ItemName, crank_locations
from .Locations import location_table, validate_locations, locked_locations, goal_locations, CK64LocationName, achievement_locations
from .Regions import region_table, CK64RegionName
from .RulesDefs import test_location, test_entrance
from .Options import CornKidz64GameOptions, Goal


_CZ64_BASE_ID = 6041000


class CornKidz64World(World):
    """The unique aura of bygone 64-bit worlds resurrected in this
    "pilot episode" 3D platformer roughly 1/3rd the size of the classics."""

    game = "Corn Kidz 64"
    topology_present = True

    item_name_to_id = {item.name.value: index + _CZ64_BASE_ID for index, item in enumerate(item_table)}
    location_name_to_id = {loc.name.value: loc.game_id for loc in location_table}
    options_dataclass = CornKidz64GameOptions

    goal_name = "Defeat Owlloh"

    def set_rules(self):
        # Add location rules.
        for i, location_data in enumerate(location_table):
            location: Location = self.multiworld.get_location(location_data.name.value, self.player)
            location.access_rule = lambda state, i=i: test_location(
                location_table[i], state, self.multiworld, self.player, self.options)

        # Add entrance rules.
        for i, region_data in enumerate(region_table):
            for o, entrance_data in enumerate(region_data.connects_to):
                entrance_name = f"{region_data.name.value} -> {entrance_data.connects_to.value}"
                entrance = self.multiworld.get_entrance(entrance_name, self.player)
                entrance.access_rule = lambda state, i=i, o=o: test_entrance(
                    region_table[i].connects_to[o], state, self.multiworld, self.player, self.options)

        # from Utils import visualize_regions
        # visualize_regions(self.multiworld.get_region("Menu", self.player), "my_world.puml")

    def create_item(self, name: str, i: int = 0) -> "CK64Item":
        item_id: int = self.item_name_to_id[name] - _CZ64_BASE_ID

        classification = item_table[item_id].classification

        if name == CK64ItemName.CrankAnxietyTower.value:
            # Anxiety tower crank is filler on non-anxiety/god runs
            if self.options.goal <= Goal.option_tower:
                classification = ItemClassification.filler
        elif name == CK64ItemName.VoidScrew.value:
            # Void screws are useless on non-god runs
            if self.options.goal <= Goal.option_anxiety:
                classification = ItemClassification.filler
        # elif name == CK64ItemName.XP.value:
        #     # XP stops becoming required at some point,
        #     # instead only counts as being useful
        #     xp_required = 200
        #     if self.options.goal == Goal.option_anxiety:
        #         xp_required = 300
        #     elif self.options.goal == Goal.option_god:
        #         xp_required = 360
        #     xp_value = 360 / self.options.xp_count
        #     xp_items_required = math.ceil(xp_required / xp_value)
        #     if i >= xp_items_required:
        #         classification = ItemClassification.useful

        return CK64Item(name, classification, item_id, self.player)

    def create_event(self, event: str, progression: bool = True):
        return CK64Item(event, ItemClassification.progression if progression else ItemClassification.filler,
                        None, self.player)

    def create_regions(self):
        player = self.player

        # Create all regions.
        regions: Dict[CK64RegionName, CK64Region] = {}
        for region_data in region_table:
            region = CK64Region(region_data.name.value, player, self.multiworld)
            regions[region_data.name.value] = region
            self.multiworld.regions.append(region)

        # Create all entrances.
        for region_data in region_table:
            parent_region = regions[region_data.name.value]
            for entrance_data in region_data.connects_to:
                entrance_name = f"{region_data.name.value} -> {entrance_data.connects_to.value}"
                child_region = regions[entrance_data.connects_to.value]
                parent_region.connect(child_region, entrance_name)

        # Create all locations.
        placed_goal = False
        for i, location_data in enumerate(location_table):
            if location_data.name in achievement_locations and not self.options.achievements:
                continue

            region = regions[location_data.region.value]
            location = CK64Location(player, location_data.name.value, location_data.game_id, region)
            region.locations.append(location)

            if location_data.name == goal_locations[self.options.goal]:
                self.goal_name = location_data.name.value
                location.place_locked_item(self.create_event(self.goal_name))
                self.multiworld.completion_condition[player] = lambda state, i=i: state.has(self.goal_name, player)
                placed_goal = True
            elif location_data.name in locked_locations:
                location.place_locked_item(self.create_event(location_data.name.value, False))

        if not placed_goal:
            raise Exception(f"[Corn Kidz 64 - {self.multiworld.get_player_name(player)}] "
                            f"Goal could not be placed properly. This game will not generate.")

    def create_items(self):
        pool = []

        # Spawn in movement items.
        if not self.options.can_jump:
            pool.append(self.create_item(CK64ItemName.Jump.value))
        if not self.options.can_punch:
            pool.append(self.create_item(CK64ItemName.Punch.value))
        if not self.options.can_climb:
            pool.append(self.create_item(CK64ItemName.Climb.value))
        if not self.options.can_ground_pound:
            pool.append(self.create_item(CK64ItemName.Slam.value))
        if not self.options.can_headbutt:
            pool.append(self.create_item(CK64ItemName.Headbutt.value))
        if not self.options.can_wall_jump:
            pool.append(self.create_item(CK64ItemName.WallJump.value))
        if not self.options.can_swim:
            pool.append(self.create_item(CK64ItemName.Swim.value))
        if not self.options.can_crouch:
            pool.append(self.create_item(CK64ItemName.Crouch.value))
        if not self.options.can_drill:
            pool.append(self.create_item(CK64ItemName.Drill.value))
        if not self.options.can_fall_warp:
            pool.append(self.create_item(CK64ItemName.FallWarp.value))

        # Spawn in cranks.
        if self.options.cranksanity:
            # Cranks will go anywhere.
            pool.extend([self.create_item(item.value) for item in crank_locations.keys()])
        else:
            # Cranks go to specific locations.
            for item_name, loc_name in crank_locations.items():
                self.multiworld.get_location(loc_name).place_locked_item(self.create_item(item_name.value))

        # Spawn in bottle caps.
        pool.extend([self.create_item(CK64ItemName.BottleCap.value) for i in range(5)])

        # Spawn in trash cans.
        pool.extend([self.create_item(CK64ItemName.TrashCan.value) for i in range(8)])

        # Spawn in disco balls.
        pool.extend([self.create_item(CK64ItemName.DiscoBall.value) for i in range(5)])

        # Spawn in rats.
        if self.options.ratsanity:
            pool.extend([self.create_item(CK64ItemName.Rat.value) for i in range(6)])

        # Spawn in void screws.
        pool.extend([self.create_item(CK64ItemName.VoidScrew.value) for i in range(11)])

        # Spawn in misc items.
        pool.append(self.create_item(CK64ItemName.MetalWorm.value))
        pool.append(self.create_item(CK64ItemName.CheeseGrater.value))

        # Spawn in HP.
        pool.extend([self.create_item(CK64ItemName.MegaDreamSoda.value) for i in range(10 - self.options.max_hp)])

        # Spawn in XP.
        pool.extend([self.create_item(CK64ItemName.XP.value, i) for i in range(self.options.xp_count)])

        # Add trap and filler items.
        junk: int = len(self.multiworld.get_unfilled_locations(self.player)) - len(pool)
        if junk < 0:
            raise Exception(f"[Corn Kidz 64 - {self.multiworld.get_player_name(self.player)}] "
                            f"Generated with too many items ({-junk}). Please reduce XP by at least this much"
                            f"(or tweak other settings).")

        trap: int = round(junk * (self.options.trap_percentage / 100))
        filler: int = junk - trap
        for i in range(trap):
            pool.append(self.create_item(self.random.choice(get_trap_items())))
        for i in range(filler):
            pool.append(self.create_item(self.random.choice(get_filler_items())))

        # Finalize item pool.
        self.multiworld.itempool += pool

    def pre_fill(self):
        world = self.multiworld
        player = self.player

        if not validate_locations():
            raise Exception(f"[Corn Kidz 64 - {world.get_player_name(player)}] "
                            f"Location validation in .apworld failed. This game will not generate.")

    def fill_slot_data(self) -> Dict[str, Any]:
        return {
            "goal": self.options.goal.value,
            "goat_color": self.options.goat_color.value,
            "xp_count": self.options.xp_count.value,
            "max_hp": self.options.max_hp.value,
            "cranksanity": self.options.cranksanity.value,
            "ratsanity": self.options.ratsanity.value,
            "achievements": self.options.achievements.value,
            "can_jump": self.options.can_jump.value,
            "can_punch": self.options.can_punch.value,
            "can_climb": self.options.can_climb.value,
            "can_ground_pound": self.options.can_ground_pound.value,
            "can_headbutt": self.options.can_headbutt.value,
            "can_wall_jump": self.options.can_wall_jump.value,
            "can_swim": self.options.can_swim.value,
            "can_crouch": self.options.can_crouch.value,
            "can_drill": self.options.can_drill.value,
            "can_fall_warp": self.options.can_fall_warp.value,
            "death_link": self.options.death_link.value
        }

    def post_fill(self) -> None:
        return

        # Just some debugging stuff for now,
        # stealing from Multiworld.can_beat_game
        state = CollectionState(self.multiworld)
        prog_locations = {location for location in self.multiworld.get_locations() if location.item
                          and location.item.advancement and location not in state.locations_checked}

        print('--- STARTING LOCATIONS ---')
        print(prog_locations)
        print('LENGTH: ' + str(len(prog_locations)))
        print('---')
        while prog_locations:
            sphere: Set[Location] = set()
            # build up spheres of collection radius.
            # Everything in each sphere is independent from each other in dependencies and only depends on lower spheres
            for location in prog_locations:
                if location.can_reach(state):
                    sphere.add(location)

            print('--- VIEWING SPHERES ---')
            print(sphere)
            print('LENGTH: ' + str(len(sphere)))
            print('---')

            if not sphere:
                # ran out of places and did not finish yet, quit
                print('RAN OUT OF SPHERES')
                return

            for location in sphere:
                print(f'{location.item}:', state.collect(location.item, True, location))
            prog_locations -= sphere

            print(state.prog_items)

            if self.multiworld.has_beaten_game(state, self.player):
                print('SUCCESS!')
                return

        print('RAN OUT OF LOCATIONS')
        return


class CK64Item(Item):
    game: str = "Corn Kidz 64"


class CK64Location(Location):
    game: str = "Corn Kidz 64"


class CK64Region(Region):
    game: str = "Corn Kidz 64"


class CK64Entrance(Entrance):
    game: str = "Corn Kidz 64"
