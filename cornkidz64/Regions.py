from dataclasses import dataclass, field
from typing import List

from enum import Enum
from .Rules import CK64Rule as Rule


class CK64RegionName(Enum):
    Menu =                        "Menu"
    NachoEmporium =               "Nacho Emporium"
    MonsterPark =                 "Lexi's Monster Park"
    MonsterParkAcrossLake =       "Lexi's Monster Park (Across Lake)"  # Either Swim or Slam+Platforming or CanReachParkTop required
    MonsterParkHouse =            "Lexi's Monster Park (House)"       # (House Crank and Jump and (Wall Jump or Climb) and Headbutt)
    MonsterParkHouseFoyer =       "Lexi's Monster Park (House Foyer)"       # House and Platforming
    MonsterParkAttic =            "Lexi's Monster Park (Attic)"  # CanReachAttic
    MonsterParkSewers =           "Lexi's Monster Park (Sewers)"  # Swim, activated by switches 103
    MonsterParkTop =              "Lexi's Monster Park (Top)"  # Foyer and Platforming (equal to CanReachParkTop)
    WollowsHollow =               "Wollow's Hollow"  # Requires CanReachUpperPark and Jump and WallJump, or switch 401 (and whatever to get corn powers)
    WollowsHollowChurch =         "Wollow's Hollow (Church)"  # Switch 212, MaxPlatforming and slam and Hollow
    WollowsHollowChurchTop =      "Wollow's Hollow (Church Top)"  # Church, MaxPlatforming
    WollowsHollowGraveyard =      "Wollow's Hollow (Graveyard)"  # WollowsHollowAboveGraveyard (or, opens via switch 242 as well)
    WollowsHollowAboveGraveyard = "Wollow's Hollow (Graveyard from Church)"  # Church and MaxPlatforming
    WollowsHollowHouse =          "Wollow's Hollow (Haunted House Ground Floor)"  # Graveyard and Level 2
    WollowsHollowHouseTop =       "Wollow's Hollow (Haunted House Top FLoor)"  # DragonPlatforming, Slam
    WollowsHollowMusic =          "Wollow's Hollow (Music Box)"  # Hollow and Level 3
    WollowsHollowRavine =         "Wollow's Hollow (Ravine)"  # Hollow, DrillMinimal
    WollowsHollowTrinkets =       "Wollow's Hollow (Trinket Shop)"  # Hollow
    WollowsHollowZombies =        "Wollow's Hollow (Zombie Chamber)"  # Trinket Shop, MaxPlatforming, Punch
    WollowsHollowRooftops =       "Wollow's Hollow (Rooftops)"  # jump, walljump, climb
    WollowsHollowCagedRooftops =  "Wollow's Hollow (Caged Rooftop)"  # WollowsHollowRooftops and headbutt
    WollowsHollowDrillChamber =   "Wollow's Hollow (Drill Chamber)"  # WollowsHollowCagedRooftops
    WollowsHollowZooOutside =     "Wollow's Hollow (Outside Zoo)"  # Hollow, jump, walljump, headbutt, drill
    WollowsHollowZoo =            "Wollow's Hollow (Sanitary Zoo)"  # ZooOutside, drill down, slam, jump headbutt. Clean zoo trigger is 202
    WollowsHollowCave =           "Wollow's Hollow (Dragon Cave)"  # Graveyard and AllTombstones and Drill and Climb and Jump and WallJump
    WollowsHollowTree =           "Wollow's Hollow (Tree)"
    WollowsHollowTreeSideRoom =   "Wollow's Hollow (Tree Side Room)"  # BatTreeSideRoom
    Tower =                       "Tower"
    AnxietyTower =                "Anxiety Tower"
    SomeOtherPlace =              "Some Other Place"  # Hollow, Jump, Headbutt, Climb or WallJump


@dataclass
class CK64EntranceData:
    connects_to: CK64RegionName
    rules_a: List[Rule] = field(default_factory=list)
    rules_b: List[Rule] = field(default_factory=list)
    rules_c: List[Rule] = field(default_factory=list)


@dataclass
class CK64RegionData:
    name: CK64RegionName
    connects_to: List[CK64EntranceData] = field(default_factory=list)


region_table: List[CK64RegionData] = [
    CK64RegionData(
        CK64RegionName.Menu,
        [
            CK64EntranceData(CK64RegionName.NachoEmporium)
        ]
    ),

    CK64RegionData(
        CK64RegionName.NachoEmporium,
        [
            CK64EntranceData(CK64RegionName.MonsterPark),
            CK64EntranceData(
                CK64RegionName.WollowsHollow,
                [Rule.CanReachParkTop, Rule.Jump, Rule.WallJump]
            ),
            CK64EntranceData(
                CK64RegionName.Tower,
                [Rule.PostOwllohDefeated]
            ),
            CK64EntranceData(
                CK64RegionName.AnxietyTower,
                [Rule.PostOwllohDefeated, Rule.Level5]
            )
        ]
    ),
    # region Park
    CK64RegionData(
        CK64RegionName.MonsterPark,
        [
            CK64EntranceData(
                CK64RegionName.MonsterParkAcrossLake,
                [Rule.Swim],
                [Rule.Slam, Rule.Platforming],
            ),
            CK64EntranceData(
                CK64RegionName.MonsterParkHouse,
                [Rule.CrankMonsterParkHouseEntry,
                 Rule.Jump, Rule.WallJump_Or_Headbutt]
            ),
            CK64EntranceData(
                CK64RegionName.MonsterParkAttic,
                [Rule.Platforming, Rule.VerticalHeadbutt]
            ),
            CK64EntranceData(
                CK64RegionName.MonsterParkSewers,
                [Rule.Swim]
            )
        ]
    ),
    CK64RegionData(CK64RegionName.MonsterParkAcrossLake),
    CK64RegionData(
        CK64RegionName.MonsterParkHouse,
        [
            CK64EntranceData(
                CK64RegionName.MonsterParkHouseFoyer,
                [Rule.Platforming]
            )
        ]
    ),
    CK64RegionData(
        CK64RegionName.MonsterParkHouseFoyer,
        [
            CK64EntranceData(
                CK64RegionName.MonsterParkTop,
                [Rule.Platforming]
            ),
        ]
    ),
    CK64RegionData(CK64RegionName.MonsterParkAttic),
    CK64RegionData(CK64RegionName.MonsterParkSewers),
    CK64RegionData(
        CK64RegionName.MonsterParkTop,
        [
            CK64EntranceData(
                CK64RegionName.MonsterParkAttic,
                [Rule.Jump, Rule.Headbutt, Rule.Climb]
            )
        ]
    ),
    # endregion
    # region Hollow
    CK64RegionData(
        CK64RegionName.WollowsHollow,
        [
            CK64EntranceData(
                CK64RegionName.WollowsHollowChurch,
                [Rule.MaxPlatforming, Rule.Slam]
            ),
            CK64EntranceData(
                CK64RegionName.WollowsHollowMusic,
                [Rule.Level3]
            ),
            CK64EntranceData(
                CK64RegionName.WollowsHollowRavine,
                [Rule.DrillMinimal]
            ),
            CK64EntranceData(CK64RegionName.WollowsHollowTrinkets),
            CK64EntranceData(
                CK64RegionName.WollowsHollowRooftops,
                [Rule.Jump, Rule.WallJump, Rule.Climb]
            ),
            CK64EntranceData(
                CK64RegionName.WollowsHollowZooOutside,
                [Rule.Jump, Rule.WallJump, Rule.Headbutt, Rule.Drill]
            ),
            CK64EntranceData(
                CK64RegionName.WollowsHollowTree,
                [Rule.CanReachFlippedHollow, Rule.MaxPlatforming, Rule.Level3],
                [Rule.PostOwllohDefeated, Rule.Platforming]
            ),
            CK64EntranceData(
                CK64RegionName.WollowsHollowTreeSideRoom,
                [Rule.CanReachFlippedHollow, Rule.CrankZooSide,
                 Rule.Jump, Rule.Drill, Rule.Headbutt, Rule.WallJump]
            ),
            CK64EntranceData(
                CK64RegionName.SomeOtherPlace,
                [Rule.Jump, Rule.Headbutt, Rule.WallJump_Or_Climb]
            )
        ]
    ),
    CK64RegionData(
        CK64RegionName.WollowsHollowChurch,
        [
            CK64EntranceData(
                CK64RegionName.WollowsHollowAboveGraveyard,
                [Rule.MaxPlatforming]
            ),
            CK64EntranceData(
                CK64RegionName.WollowsHollowChurchTop,
                [Rule.MaxPlatforming],
            )
        ]
    ),
    CK64RegionData(CK64RegionName.WollowsHollowChurchTop),
    CK64RegionData(
        CK64RegionName.WollowsHollowGraveyard,
        [
            CK64EntranceData(
                CK64RegionName.WollowsHollow,
                [Rule.Jump, Rule.Headbutt]
            ),
            CK64EntranceData(
                CK64RegionName.WollowsHollowHouse,
                [Rule.Level2]
            ),
            CK64EntranceData(
                CK64RegionName.WollowsHollowCave,
                [Rule.AllTombstones, Rule.Drill,
                 Rule.Climb, Rule.Jump, Rule.WallJump],
            ),
            CK64EntranceData(
                CK64RegionName.WollowsHollowHouseTop,
                [Rule.DragonPlatforming, Rule.Jump, Rule.Slam]
            )
        ]
    ),
    CK64RegionData(
        CK64RegionName.WollowsHollowAboveGraveyard,
        [
            CK64EntranceData(CK64RegionName.WollowsHollowGraveyard)
        ]
    ),
    CK64RegionData(CK64RegionName.WollowsHollowHouse),
    CK64RegionData(CK64RegionName.WollowsHollowHouseTop),
    CK64RegionData(CK64RegionName.WollowsHollowMusic),
    CK64RegionData(CK64RegionName.WollowsHollowRavine),
    CK64RegionData(
        CK64RegionName.WollowsHollowTrinkets,
        [
            CK64EntranceData(
                CK64RegionName.WollowsHollowZombies,
                [Rule.MaxPlatforming, Rule.Punch]
            )
        ]
    ),
    CK64RegionData(CK64RegionName.WollowsHollowZombies),
    CK64RegionData(
        CK64RegionName.WollowsHollowRooftops,
        [
            CK64EntranceData(
                CK64RegionName.WollowsHollowCagedRooftops,
                [Rule.Jump, Rule.Headbutt, Rule.Climb]
            )
        ]
    ),
    CK64RegionData(
        CK64RegionName.WollowsHollowCagedRooftops,
        [
            CK64EntranceData(
                CK64RegionName.WollowsHollowDrillChamber,
                [Rule.Jump, Rule.Climb]
            )
        ]
    ),
    CK64RegionData(CK64RegionName.WollowsHollowDrillChamber),
    CK64RegionData(
        CK64RegionName.WollowsHollowZooOutside,
        [
            CK64EntranceData(
                CK64RegionName.WollowsHollowZoo,
                [Rule.Jump, Rule.WallJump, Rule.Headbutt, Rule.Drill]
            )
        ]
    ),
    CK64RegionData(CK64RegionName.WollowsHollowZoo),
    CK64RegionData(CK64RegionName.WollowsHollowCave),
    CK64RegionData(CK64RegionName.WollowsHollowTree),
    CK64RegionData(CK64RegionName.WollowsHollowTreeSideRoom),
    # endregion
    # region Misc
    CK64RegionData(CK64RegionName.Tower),
    CK64RegionData(CK64RegionName.AnxietyTower),
    CK64RegionData(CK64RegionName.SomeOtherPlace),
    # endregion
]
