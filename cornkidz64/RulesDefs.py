import math
from typing import Dict, Callable

from .Items import CK64ItemName as Item
from .Options import CornKidz64GameOptions
from .Locations import CK64LocationData
from .Regions import CK64EntranceData, CK64RegionName
from BaseClasses import CollectionState, MultiWorld, Location, Entrance

from .Rules import CK64Rule


rules_to_func: Dict[CK64Rule, Callable] = {}


def rule(rule: CK64Rule):
    def decorator(f):
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)
        rules_to_func[rule] = f
        return wrapper
    return decorator


"""
Rule definitions
"""


def get_xp_count(state: CollectionState, player: int, options: CornKidz64GameOptions) -> int:
    total_xp = 360
    curr_xp = math.floor((total_xp / options.xp_count) * state.count(Item.XP.value, player))
    return curr_xp


@rule(CK64Rule.Level2)
def Level2(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return get_xp_count(state, player, options) >= 70


@rule(CK64Rule.Level3)
def Level3(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return get_xp_count(state, player, options) >= 140


@rule(CK64Rule.Level4)
def Level4(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return get_xp_count(state, player, options) >= 200


@rule(CK64Rule.Level5)
def Level5(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return get_xp_count(state, player, options) >= 300


@rule(CK64Rule.Level6)
def Level6(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return get_xp_count(state, player, options) >= 360


@rule(CK64Rule.AllBottlecaps)
def AllBottlecaps(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return state.has(Item.BottleCap.value, player, 5)


@rule(CK64Rule.AllTrashcans)
def AllTrashcans(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return state.has(Item.TrashCan.value, player, 8)


@rule(CK64Rule.AllDiscoBalls)
def AllDiscoBalls(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return state.has(Item.DiscoBall.value, player, 5)


@rule(CK64Rule.CheeseGrater)
def CheeseGrater(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return state.has(Item.CheeseGrater.value, player)


@rule(CK64Rule.AllTombstones)
def AllTombstones(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return state.can_reach(CK64RegionName.WollowsHollowGraveyard.value, None, player) and \
            BreakGroundedObject(state, world, player, options)


@rule(CK64Rule.AtLeastFourVoidScrews)
def AtLeastFourVoidScrews(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return state.item_count(Item.VoidScrew.value, player) >= 4


@rule(CK64Rule.AllVoidScrews)
def AllVoidScrews(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return state.has(Item.VoidScrew.value, player, 11)


@rule(CK64Rule.AnyVoidScrew)
def AnyVoidScrew(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return state.has(Item.VoidScrew.value, player)


@rule(CK64Rule.AnyHPItem)
def AnyHPItem(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return state.has(Item.MegaDreamSoda.value, player)


@rule(CK64Rule.Jump)
def Jump(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return state.has(Item.Jump.value, player) or options.can_jump


@rule(CK64Rule.Punch)
def Punch(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return state.has(Item.Punch.value, player) or options.can_punch


@rule(CK64Rule.Climb)
def Climb(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return state.has(Item.Climb.value, player) or options.can_climb


@rule(CK64Rule.Slam)
def Slam(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return state.has(Item.Slam.value, player) or options.can_ground_pound


@rule(CK64Rule.Headbutt)
def Headbutt(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return state.has(Item.Headbutt.value, player) or options.can_headbutt


@rule(CK64Rule.WallJump)
def WallJump(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return state.has(Item.WallJump.value, player) or options.can_wall_jump


@rule(CK64Rule.Swim)
def Swim(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return state.has(Item.Swim.value, player) or options.can_swim


@rule(CK64Rule.Crouch)
def Crouch(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return state.has(Item.Crouch.value, player) or options.can_crouch


@rule(CK64Rule.Drill)
def Drill(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return state.has(Item.Drill.value, player) or options.can_drill


@rule(CK64Rule.FallWarp)
def FallWarp(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return state.has(Item.FallWarp.value, player) or options.can_fall_warp


@rule(CK64Rule.TowerMovement)
def TowerMovement(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return Jump(state, world, player, options) and \
            Punch(state, world, player, options) and \
            Climb(state, world, player, options) and \
            Slam(state, world, player, options) and \
            Headbutt(state, world, player, options) and \
            WallJump(state, world, player, options) and \
            Crouch(state, world, player, options) and \
            Drill(state, world, player, options)


@rule(CK64Rule.WallJump_Or_Climb)
def WallJump_Or_Climb(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return WallJump(state, world, player, options) or \
            Climb(state, world, player, options)


@rule(CK64Rule.Jump_Or_Headbutt)
def Jump_Or_Headbutt(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return Jump(state, world, player, options) or \
            Headbutt(state, world, player, options)


@rule(CK64Rule.WallButton)
def WallButton(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return Jump(state, world, player, options) and \
            Headbutt(state, world, player, options)


@rule(CK64Rule.HighClimb)
def HighClimb(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return Jump(state, world, player, options) and \
            Climb(state, world, player, options)


@rule(CK64Rule.Climb_Or_Headbutt)
def Climb_Or_Headbutt(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return Climb(state, world, player, options) or \
            Headbutt(state, world, player, options)


@rule(CK64Rule.WallJump_Or_Headbutt)
def WallJump_Or_Headbutt(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return WallJump(state, world, player, options) or \
            Headbutt(state, world, player, options)


@rule(CK64Rule.WallJump_Or_Slam)
def WallJump_Or_Slam(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return WallJump(state, world, player, options) or \
            Slam(state, world, player, options)


@rule(CK64Rule.Platforming)
def Platforming(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return Jump(state, world, player, options) and \
            WallJump(state, world, player, options) and \
            Climb(state, world, player, options)


@rule(CK64Rule.MaxPlatforming)
def MaxPlatforming(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return Platforming(state, world, player, options) and \
            Headbutt(state, world, player, options)


@rule(CK64Rule.BreakGroundedObject)
def BreakGroundedObject(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return Headbutt(state, world, player, options) and \
            (Jump(state, world, player, options) or
            Crouch(state, world, player, options))


@rule(CK64Rule.VerticalHeadbutt)
def VerticalHeadbutt(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return Crouch(state, world, player, options) and \
            Headbutt(state, world, player, options)


@rule(CK64Rule.BreakCrystal)
def BreakCrystal(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return Jump(state, world, player, options) and \
        Headbutt(state, world, player, options)


@rule(CK64Rule.BreakTrashcan)
def BreakTrashcan(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return Punch(state, world, player, options) or \
            (Jump(state, world, player, options) and Headbutt(state, world, player, options)) or \
            (Crouch(state, world, player, options) and Headbutt(state, world, player, options)) or \
            (Jump(state, world, player, options) and Slam(state, world, player, options))


@rule(CK64Rule.BombBird)
def BombBird(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return BreakGroundedObject(state, world, player, options)


@rule(CK64Rule.OpenChest)
def OpenChest(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return Jump(state, world, player, options) and \
        Headbutt(state, world, player, options)


@rule(CK64Rule.Chameleon)
def Chameleon(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return Jump(state, world, player, options) and \
        Headbutt(state, world, player, options)


@rule(CK64Rule.DrillDownwards)
def DrillDownwards(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return Jump(state, world, player, options) and \
            Slam(state, world, player, options) and \
            Drill(state, world, player, options)


@rule(CK64Rule.DrillWall)
def DrillWall(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return Jump(state, world, player, options) and \
            Headbutt(state, world, player, options) and \
            Drill(state, world, player, options)


@rule(CK64Rule.DrillMinimal)
def DrillMinimal(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return Drill(state, world, player, options) and \
            (Headbutt(state, world, player, options) or
            Slam(state, world, player, options))


@rule(CK64Rule.CanBeatZombieTurtle)
def CanBeatZombieTurtle(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return BreakGroundedObject(state, world, player, options) and \
            Punch(state, world, player, options) and \
            Slam(state, world, player, options)


@rule(CK64Rule.CanGetHurt)
def CanGetHurt(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    if options.max_hp > 1:
        return True
    return state.has(Item.MegaDreamSoda.value, player)


@rule(CK64Rule.DragonPlatforming)
def DragonPlatforming(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return state.has(Item.CrankDragonWall.value, player) and \
            Jump(state, world, player, options) and \
            WallJump(state, world, player, options) and \
            Headbutt(state, world, player, options)


@rule(CK64Rule.CanFreeHauntedHouseBird)
def CanFreeHauntedHouseBird(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return state.can_reach(CK64RegionName.WollowsHollowHouseTop.value, None, player) and \
            Jump(state, world, player, options) and \
            Slam(state, world, player, options) and \
            CanBeatZombieTurtle(state, world, player, options)


@rule(CK64Rule.CanUseMetalWorm)
def CanUseMetalWorm(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return CanClimbInteriorTree(state, world, player, options) and \
            (CanCleanZoo(state, world, player, options) or CanGetHurt(state, world, player, options)) and \
            Jump(state, world, player, options) and \
            Headbutt(state, world, player, options)


@rule(CK64Rule.CanReachAttic)
def CanReachAttic(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return (Platforming(state, world, player, options) and VerticalHeadbutt(state, world, player, options)) or \
            (CanReachParkTop(state, world, player, options) and Jump(state, world, player, options) and
            Climb(state, world, player, options) and Headbutt(state, world, player, options))


@rule(CK64Rule.CanReachParkTop)
def CanReachParkTop(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return state.can_reach(CK64RegionName.MonsterParkTop.value, None, player)


@rule(CK64Rule.CanReachRooftops)
def CanReachRooftops(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return state.can_reach(CK64RegionName.WollowsHollowRooftops.value, None, player)


@rule(CK64Rule.CanReachCagedRooftops)
def CanReachCagedRooftops(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return state.can_reach(CK64RegionName.WollowsHollowCagedRooftops.value, None, player)


@rule(CK64Rule.CanReachGraveyard)
def CanReachGraveyard(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return state.can_reach(CK64RegionName.WollowsHollowGraveyard.value, None, player)


@rule(CK64Rule.CanReachGraveyardTop)
def CanReachGraveyardTop(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return state.can_reach(CK64RegionName.WollowsHollowAboveGraveyard.value, None, player)


@rule(CK64Rule.CanReachFlippedHollow)
def CanReachFlippedHollow(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return state.can_reach(CK64RegionName.WollowsHollowDrillChamber.value, None, player) and \
            Slam(state, world, player, options) and \
            Drill(state, world, player, options) and \
            AllDiscoBalls(state, world, player, options)


@rule(CK64Rule.CanEnterFountain)
def CanEnterFountain(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return CanReachFlippedHollow(state, world, player, options) and \
            Jump(state, world, player, options) and \
            Headbutt(state, world, player, options) and \
            (Climb(state, world, player, options) or WallJump(state, world, player, options)) and \
            Swim(state, world, player, options)


@rule(CK64Rule.CanClimbInteriorTree)
def CanClimbInteriorTree(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return state.can_reach(CK64RegionName.WollowsHollowTree.value, None, player) and \
            MaxPlatforming(state, world, player, options) and \
            Slam(state, world, player, options) and \
            Drill(state, world, player, options)


@rule(CK64Rule.BatTreeSideRoom)
def BatTreeSideRoom(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return CanReachFlippedHollow(state, world, player, options) and \
            state.has(Item.CrankZooWall.value, player) and \
            Jump(state, world, player, options) and \
            Drill(state, world, player, options) and \
            Headbutt(state, world, player, options) and \
            WallJump(state, world, player, options)


@rule(CK64Rule.BatTreeSideRoomCollectables)
def BatTreeSideRoomCollectables(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return state.can_reach(CK64RegionName.WollowsHollowTreeSideRoom.value, None, player) and \
            (Slam(state, world, player, options) or
            WallJump(state, world, player, options)) and \
            Headbutt(state, world, player, options)


@rule(CK64Rule.CrankMonsterParkHouseEntry)
def CrankMonsterParkHouseEntry(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return state.has(Item.CrankHouseEntry.value, player)


@rule(CK64Rule.CrankHollowDragonWall)
def CrankHollowDragonWall(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return state.has(Item.CrankDragonWall.value, player)


@rule(CK64Rule.CrankZooSide)
def CrankZooSide(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return state.has(Item.CrankZooWall.value, player)


@rule(CK64Rule.CanCleanZoo)
def CanCleanZoo(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    if options.ratsanity:
        return state.can_reach(CK64RegionName.WollowsHollowZoo.value, None, player) and \
                state.has(Item.Rat.value, player, 6)
    else:
        return state.can_reach(CK64RegionName.WollowsHollowZoo.value, None, player) and \
            MaxPlatforming(state, world, player, options) and \
            Drill(state, world, player, options) and \
            Punch(state, world, player, options)


@rule(CK64Rule.CanDefeatOwlloh)
def CanDefeatOwlloh(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return CanClimbInteriorTree(state, world, player, options) and \
        Level4(state, world, player, options)


@rule(CK64Rule.AnxietyTowerChecks)
def AnxietyTowerChecks(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return PostOwllohDefeated(state, world, player, options) and \
        Level5(state, world, player, options) and \
        TowerMovement(state, world, player, options)


@rule(CK64Rule.PostOwllohDefeated)
def PostOwllohDefeated(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return CanDefeatOwlloh(state, world, player, options)


@rule(CK64Rule.CanAccessGraveyardBomb)
def CanAccessGraveyardBomb(state: CollectionState, world: MultiWorld, player: int, options: CornKidz64GameOptions):
    return CanReachGraveyard(state, world, player, options) and \
            Swim(state, world, player, options) and \
            BombBird(state, world, player, options) and \
            Platforming(state, world, player, options)


"""
Meta location testing
"""


def test_location(location_data: CK64LocationData, state: CollectionState,
                  world: MultiWorld, player: int,
                  options: CornKidz64GameOptions) -> bool:
    test_a = all(rules_to_func[r](state, world, player, options) for r in location_data.rules_a) if location_data.rules_a else False
    test_b = all(rules_to_func[r](state, world, player, options) for r in location_data.rules_b) if location_data.rules_b else False
    if location_data.rules_a and location_data.rules_b:
        return test_a or test_b
    elif location_data.rules_a:
        return test_a
    else:
        return True


def test_entrance(entrance_data: CK64EntranceData, state: CollectionState,
                  world: MultiWorld, player: int,
                  options: CornKidz64GameOptions) -> bool:
    test_a = all(rules_to_func[r](state, world, player, options) for r in entrance_data.rules_a) if entrance_data.rules_a else False
    test_b = all(rules_to_func[r](state, world, player, options) for r in entrance_data.rules_b) if entrance_data.rules_b else False
    test_c = all(rules_to_func[r](state, world, player, options) for r in entrance_data.rules_c) if entrance_data.rules_c else False
    if entrance_data.rules_a and entrance_data.rules_b and entrance_data.rules_c:
        return test_a or test_b or test_c
    elif entrance_data.rules_a and entrance_data.rules_b:
        return test_a or test_b
    elif entrance_data.rules_a:
        return test_a
    else:
        return True
