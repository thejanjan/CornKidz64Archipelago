from dataclasses import dataclass
from typing import List, Dict
from enum import Enum

from BaseClasses import ItemClassification
from .Locations import CK64LocationName


class CK64ItemName(Enum):
    # Movement
    Jump     = "Jump"
    Punch    = "Punch"
    Climb    = "Climb"
    Slam     = "Slam"
    Headbutt = "Headbutt"
    WallJump = "Wall Jump"
    Swim     = "Swim"
    Crouch   = "Crouch"
    Drill    = "Drill"  # gives UpgradeItem 1
    FallWarp = "Fall Warp"  # gives UpgradeItem 2

    # Cranks
    CrankHouseEntry   = "Crank (Park Entrance)"         # switch 108
    CrankDragonWall   = "Crank (Hollow Elevator)"       # switch 228
    CrankZooWall      = "Crank (Hollow Question Mark)"  # switch 229
    CrankAnxietyTower = "Crank (Anxiety Tower)"         # switch 410

    # Collectables
    BottleCap = "Bottle Cap"
    TrashCan  = "Trash Can"
    DiscoBall = "Disco Ball"
    Rat       = "Justina"     # TODO determine trigger later
    MetalWorm = "Metal Worm"  # switch/save trigger 236
    MegaDreamSoda = "Mega Dream Soda"
    CheeseGrater = "Cheese Grater"
    VoidScrew = "Void Screw"

    # Traps
    SlapTrap = 'Slap Trap'
    SlipTrap = 'Slip Trap'

    # Filler
    DreamSoda = 'Dream Soda'

    # Progression
    XP = 'Experience'


@dataclass
class CK64ItemData:
    name: CK64ItemName
    classification: ItemClassification


item_table: List[CK64ItemData] = [
    # region Movement
    CK64ItemData(
        CK64ItemName.Jump,
        ItemClassification.progression,
    ),
    CK64ItemData(
        CK64ItemName.Punch,
        ItemClassification.progression,
    ),
    CK64ItemData(
        CK64ItemName.Climb,
        ItemClassification.progression,
    ),
    CK64ItemData(
        CK64ItemName.Slam,
        ItemClassification.progression,
    ),
    CK64ItemData(
        CK64ItemName.Headbutt,
        ItemClassification.progression,
    ),
    CK64ItemData(
        CK64ItemName.WallJump,
        ItemClassification.progression,
    ),
    CK64ItemData(
        CK64ItemName.Swim,
        ItemClassification.progression,
    ),
    CK64ItemData(
        CK64ItemName.Crouch,
        ItemClassification.progression,
    ),
    CK64ItemData(
        CK64ItemName.Drill,
        ItemClassification.progression,
    ),
    CK64ItemData(
        CK64ItemName.FallWarp,
        ItemClassification.useful,
    ),
    # endregion
    # region Cranks
    CK64ItemData(
        CK64ItemName.CrankHouseEntry,
        ItemClassification.progression,
    ),
    CK64ItemData(
        CK64ItemName.CrankDragonWall,
        ItemClassification.progression,
    ),
    CK64ItemData(
        CK64ItemName.CrankZooWall,
        ItemClassification.progression,
    ),
    CK64ItemData(
        CK64ItemName.CrankAnxietyTower,
        ItemClassification.progression,
    ),
    # endregion
    # region Collectables
    CK64ItemData(
        CK64ItemName.BottleCap,
        ItemClassification.progression,
    ),
    CK64ItemData(
        CK64ItemName.TrashCan,
        ItemClassification.progression,
    ),
    CK64ItemData(
        CK64ItemName.DiscoBall,
        ItemClassification.progression,
    ),
    CK64ItemData(
        CK64ItemName.Rat,
        ItemClassification.progression,
    ),
    CK64ItemData(
        CK64ItemName.MetalWorm,
        ItemClassification.progression,
    ),
    CK64ItemData(
        CK64ItemName.MegaDreamSoda,
        ItemClassification.useful,
    ),
    CK64ItemData(
        CK64ItemName.CheeseGrater,
        ItemClassification.progression,
    ),
    CK64ItemData(
        CK64ItemName.VoidScrew,
        ItemClassification.progression,
    ),
    # endregion
    # region Progression
    CK64ItemData(
        CK64ItemName.XP,
        ItemClassification.progression,
    ),
    # endregion
    # region Filler
    CK64ItemData(
        CK64ItemName.DreamSoda,
        ItemClassification.filler,
    ),
    # endregion
    # region Traps
    CK64ItemData(
        CK64ItemName.SlapTrap,
        ItemClassification.trap,
    ),
    CK64ItemData(
        CK64ItemName.SlipTrap,
        ItemClassification.trap,
    ),
    # endregion
]


def get_trap_items() -> List[str]:
    return [item_data.name.value for item_data in item_table
            if item_data.classification == ItemClassification.trap]


def get_filler_items() -> List[str]:
    return [item_data.name.value for item_data in item_table
            if item_data.classification == ItemClassification.filler]


crank_locations: Dict[CK64ItemName, CK64LocationName] = {
    CK64ItemName.CrankHouseEntry:   CK64LocationName.CrankMonsterParkAcrossLake,
    CK64ItemName.CrankDragonWall:   CK64LocationName.CrankHollowHauntedHouseGroundFloor,
    CK64ItemName.CrankZooWall:      CK64LocationName.CrankHollowRavine,
    CK64ItemName.CrankAnxietyTower: CK64LocationName.CrankAnxietyTower,
}
