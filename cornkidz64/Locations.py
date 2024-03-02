from typing import List
from dataclasses import dataclass, field
from enum import Enum

from BaseClasses import LocationProgressType
from .Options import Goal
from .Regions import CK64RegionName as Region
from .Rules import CK64Rule as Rule


class CK64LocationName(Enum):
    CubeParkNearSlide =								"Cube (Park Near Slide)"
    CubeParkSlide =									"Cube (Park Slide)"
    CubeParkUnderSlide =							"Cube (Park Under Slide)"
    CubeParkBouncyMoose =							"Cube (Park Bouncy Moose)"
    CubeParkTopHat =								"Cube (Park Top Hat)"
    CubeParkWater1 =								"Cube (Park Water 1)"
    CubeParkWater2 =								"Cube (Park Water 2)"
    CubeParkAcrossWater1 =							"Cube (Park Across Water #1)"
    CubeParkAcrossWater2 =							"Cube (Park Across Water #2)"
    CubeParkAcrossWater3 =							"Cube (Park Across Water #3)"
    CubeParkAcrossWater4 =							"Cube (Park Across Water #4)"
    CubeStoneStatue1 =								"Cube (Stone Statue #1)"
    CubeStoneStatue2 =								"Cube (Stone Statue #2)"
    CubeStoneStatue3 =								"Cube (Stone Statue #3)"
    CubeParkFence =									"Cube (Park Fence)"
    CubeParkLowerSlamPillar =						"Cube (Park Lower Slam Pillar)"
    CubeParkUpperSlamPillar =						"Cube (Park Upper Slam Pillar)"
    CubeParkAtticDrill1 =							"Cube (Park Attic Drill #1)"
    CubeParkAtticDrill2 =							"Cube (Park Attic Drill #2)"
    CubeParkAtticHigh1 =							"Cube (Park Attic High #1)"
    CubeParkAtticHigh2 =							"Cube (Park Attic High #2)"
    CubeParkAtticHallway =							"Cube (Park Attic Hallway)"
    CubeParkHouseBookcase =							"Cube (Park House Bookcase)"
    CubeParkHouseFoyer1 =							"Cube (Park House Foyer #1)"
    CubeParkHouseFoyer2 =							"Cube (Park House Foyer #2)"
    CubeParkHouseFoyer3 =							"Cube (Park House Foyer #3)"
    CubeParkHouseFoyerTower =						"Cube (Park House Foyer Tower)"
    CubeParkTopBouncyMoose =						"Cube (Park Top Bouncy Moose)"
    CubeParkTopButtonChallenge1 =					"Cube (Park Top Button Challenge #1)"
    CubeParkTopButtonChallenge2 =					"Cube (Park Top Button Challenge #2)"
    CubeParkTopButtonChallenge3 =					"Cube (Park Top Button Challenge #3)"
    CubeParkDrillPastLake =							"Cube (Park Drill Past Lake)"
    ScrewParkLakeBombYeet =						    "Screw (Park Lake Bomb Yeet)"
    ScrewParkAtticScrewScrew =						"Screw (Park Attic Screw Screw)"
    ScrewParkAtticDrill =							"Screw (Park Attic Drill)"
    ScrewParkAboveCrank =							"Screw (Park Above Crank)"
    ScrewParkHouseFoyer =							"Screw (Park House Foyer)"
    ScrewParkTopWallJumpChallenge =					"Screw (Park Top Wall Jump Challenge)"
    ChameleonPark =									"Chameleon (Park)"
    ChameleonInterior =								"Chameleon (Interior)"
    CrystalParkAttic =								"Crystal (Park Attic)"
    CrystalGarbageGrump =							"Crystal (Garbage Grump)"
    MirrorParkSewers =								"Mirror (Park Sewers)"
    MirrorFoyerLevel3 =								"Mirror (Foyer Level 3)"
    CrankMonsterParkAcrossLake =					"Crank (Monster Park Across Lake)"
    TrashCanPark =									"Trash Can (Park)"
    TrashCanAttic1 =								"Trash Can (Attic #1)"
    TrashCanAttic2 =								"Trash Can (Attic #2)"
    TrashCanSewers =								"Trash Can (Sewers)"
    TrashCanFoyer =									"Trash Can (Foyer)"
    TrashCanParkTop =								"Trash Can (Park Top)"
    TrashCanParkTopWallJumpChallenge =				"Trash Can (Park Top Wall Jump Challenge)"
    TrashCanFoyerLevel3 =							"Trash Can (Foyer Level 3)"
    CubeHollowBridge1 =								"Cube (Hollow Bridge #1)"
    CubeHollowBridge2 =								"Cube (Hollow Bridge #2)"
    CubeHollowBridge3 =								"Cube (Hollow Bridge #3)"
    CubeHollowOnTrees =								"Cube (Hollow On Trees)"
    CubeHollowLeavesUnderOwlTree =					"Cube (Hollow Leaves Under Owl Tree)"
    CubeHollowLeavesOnOwlTree =						"Cube (Hollow Leaves On Owl Tree)"
    CubeHollowPillar1 =								"Cube (Hollow Pillar #1)"
    CubeHollowPillar2 =								"Cube (Hollow Pillar #2)"
    CubeHollowTrampoline =							"Cube (Hollow Trampoline)"
    CubeHollowTrinketShop =							"Cube (Hollow Trinket Shop)"
    CubeHollowClockWallClimb1 =						"Cube (Hollow Clock Wall Climb #1)"
    CubeHollowClockWallClimb2 =						"Cube (Hollow Clock Wall Climb #2)"
    CubeHollowPillarOutsideChurch =					"Cube (Hollow Pillar Outside Church)"
    CubeHollowClockwiseVomit =						"Cube (Hollow Clockwise Vomit)"
    CubeHollowFartTunnel1 =							"Cube (Hollow Fart Tunnel #1)"
    CubeHollowFartTunnel2 =							"Cube (Hollow Fart Tunnel #2)"
    CubeHollowChurch1 =								"Cube (Hollow Church #1)"
    CubeHollowChurch2 =								"Cube (Hollow Church #2)"
    CubeHollowChurch3 =								"Cube (Hollow Church #3)"
    CubeHollowGraveyardPole1 =						"Cube (Hollow Graveyard Pole #1)"
    CubeHollowGraveyardTacoCat =					"Cube (Hollow Graveyard Taco Cat)"
    CubeHollowGraveyardPole2 =						"Cube (Hollow Graveyard Pole #2)"
    CubeHollowGraveyardBehindWetTree =				"Cube (Hollow Graveyard Behind Wet Tree)"
    CubeHollowGraveyardWater =						"Cube (Hollow Graveyard Water)"
    CubeHollowGraveyardTombstoneCode1 =				"Cube (Hollow Graveyard Tombstone Code #1)"
    CubeHollowGraveyardTombstoneCode2 =				"Cube (Hollow Graveyard Tombstone Code #2)"
    CubeHollowGraveyardTombstoneCode3 =				"Cube (Hollow Graveyard Tombstone Code #3)"
    CubeHollowBalcony1 =							"Cube (Hollow Balcony #1)"
    CubeHollowBalcony2 =							"Cube (Hollow Balcony #2)"
    CubeHollowNearBats1 =							"Cube (Hollow Near Bats #1)"
    CubeHollowNearBats2 =							"Cube (Hollow Near Bats #2)"
    CubeHollowDrillRoom1 =							"Cube (Hollow Drill Room #1)"
    CubeHollowDrillRoom2 =							"Cube (Hollow Drill Room #2)"
    CubeHollowDrillRoom3 =							"Cube (Hollow Drill Room #3)"
    CubeHollowDrillUnderRamp =						"Cube (Hollow Drill Under Ramp)"
    CubeHollowDrillBars1 =							"Cube (Hollow Drill Bars #1)"
    CubeHollowDrillBars2 =							"Cube (Hollow Drill Bars #2)"
    CubeHollowDrillUnderChurch1 =					"Cube (Hollow Drill Under Church #1)"
    CubeHollowDrillUnderChurch2 =					"Cube (Hollow Drill Under Church #2)"
    CubeHollowDrillDragonMountainside1 =			"Cube (Hollow Drill Dragon Mountainside #1)"
    CubeHollowDrillDragonMountainside2 =			"Cube (Hollow Drill Dragon Mountainside #2)"
    CubeHollowHauntedHouseTop1 =					"Cube (Hollow Haunted House Top #1)"
    CubeHollowHauntedHouseTop2 =					"Cube (Hollow Haunted House Top #2)"
    CubeHollowHauntedHouseBehindChimney =			"Cube (Hollow Haunted House Behind Chimney)"
    CubeHollowRavine1 =								"Cube (Hollow Ravine #1)"
    CubeHollowRavine2 =								"Cube (Hollow Ravine #2)"
    CubeHollowRavine3 =								"Cube (Hollow Ravine #3)"
    CubeHollowFencedAcrossRavine =					"Cube (Hollow Fenced Across Ravine)"
    CubeHollowMusicBoxSwim1 =						"Cube (Hollow Music Box Swim #1)"
    CubeHollowMusicBoxSwim2 =						"Cube (Hollow Music Box Swim #2)"
    CubeHollowBrickWall1 =							"Cube (Hollow Brick Wall #1)"
    CubeHollowBrickWall2 =							"Cube (Hollow Brick Wall #2)"
    CubeHollowBehindSanitaryZoo =					"Cube (Hollow Behind Sanitary Zoo)"
    CubeHollowSpiderOutsideZoo =					"Cube (Hollow Spider Outside Zoo)"
    CubeFlippedHollowDragonCrankDrill =				"Cube (Flipped Hollow Dragon Crank Drill)"
    CubeFlippedHollowFountainSwim1 =				"Cube (Flipped Hollow Fountain Swim #1)"
    CubeFlippedHollowFountainSwim2 =				"Cube (Flipped Hollow Fountain Swim #2)"
    CubeFlippedHollowFountainSwim3 =				"Cube (Flipped Hollow Fountain Swim #3)"
    CubeFlippedHollowFountainSwim4 =				"Cube (Flipped Hollow Fountain Swim #4)"
    CubeHollowTreeFishTimer =						"Cube (Hollow Tree Fish Timer)"
    CubeHollowTreeSwim =							"Cube (Hollow Tree Swim)"
    CubeHollowTreeNearMetalWorm =					"Cube (Hollow Tree Near Metal Worm)"
    CubeHollowGraveyardSpiderCaveDrill =			"Cube (Hollow Graveyard Spider Cave Drill)"
    ScrewHollowTownClock =							"Screw (Hollow Town Clock)"
    ScrewHollowDrillTowerAlcove =					"Screw (Hollow Drill Tower Alcove)"
    ScrewHollowBehindHauntedHouse =					"Screw (Hollow Behind Haunted House)"
    ScrewHollowDragonCave =							"Screw (Hollow Dragon Cave)"
    ScrewHollowLargeCrankPit =						"Screw (Hollow Large Crank Pit)"
    ScrewHollowZoo =								"Screw (Hollow Zoo)"
    ScrewFlippedHollowTreeSideRoom =				"Screw (Flipped Hollow Tree Side Room)"
    ScrewHollowTreeHighScrew =						"Screw (Hollow Tree High Screw)"
    ScrewHollowTreeLowScrew =						"Screw (Hollow Tree Low Screw)"
    ChameleonHollowBush =							"Chameleon (Hollow Bush)"
    ChameleonHollowGraveyard =						"Chameleon (Hollow Graveyard)"
    CrystalHollowTimedFountain =					"Crystal (Hollow Timed Fountain)"
    CrystalHollowChurchBell =						"Crystal (Hollow Church Bell)"
    CrystalHollowGraveyardSpiderReward =			"Crystal (Hollow Graveyard Spider Reward)"
    CrystalHollowDrillPillar =						"Crystal (Hollow Drill Pillar)"
    CrystalHollowHauntedHouseFreeBird =				"Crystal (Hollow Haunted House Free Bird)"
    CrystalHollowDragonCave =						"Crystal (Hollow Dragon Cave)"
    CrystalHollowAboveEntry =						"Crystal (Hollow Above Entry)"
    CrystalHollowZombieChamber =					"Crystal (Hollow Zombie Chamber)"
    CrystalHollowFreeStuckPig =						"Crystal (Hollow Free Stuck Pig)"
    CrystalHollowBombChurchPillar =					"Crystal (Hollow Bomb Church Pillar)"
    CrystalFlippedHollowCounterclockwiseVomit =		"Crystal (Flipped Hollow Counterclockwise Vomit)"
    CrystalFlippedHollowGassyMoosey =				"Crystal (Flipped Hollow Gassy Moosey)"
    MirrorHollowGraveyard =							"Mirror (Hollow Graveyard)"
    MirrorHollowZooSideCrank =						"Mirror (Hollow Zoo-Side Crank)"
    MirrorFlippedHollowDragonCrank =				"Mirror (Flipped Hollow Dragon Crank)"
    MirrorZooMetalWorm =							"Mirror (Zoo Metal Worm)"
    CrankHollowHauntedHouseGroundFloor =			"Crank (Hollow Haunted House Ground Floor)"
    CrankHollowRavine =								"Crank (Hollow Ravine)"
    DiscoBallHollowTrinketShop =					"Disco Ball (Hollow Trinket Shop)"
    DiscoBallHollowDragonChest =					"Disco Ball (Hollow Dragon Chest)"
    DiscoBallHollowMusicBox =						"Disco Ball (Hollow Music Box)"
    DiscoBallHollowZombieChamber =					"Disco Ball (Hollow Zombie Chamber)"
    DiscoBallHollowCleanZoo =						"Disco Ball (Hollow Clean Zoo)"
    BottleCapHollowGraveyard =						"Bottle Cap (Hollow Graveyard)"
    BottleCapHollowGraveyardInsideWetTree =			"Bottle Cap (Hollow Graveyard Inside Wet Tree)"
    BottleCapHollowRavineClimb =					"Bottle Cap (Hollow Ravine Climb)"
    BottleCapHollowZooRooftop =						"Bottle Cap (Hollow Zoo Rooftop)"
    BottleCapHollowZooSideCrank =					"Bottle Cap (Hollow Zoo-Side Crank)"
    VoidScrewParkHouse =							"Void Screw (Park House)"
    VoidScrewHollowOutsideTrinketShop =				"Void Screw (Hollow Outside Trinket Shop)"
    VoidScrewHollowChurch =							"Void Screw (Hollow Church)"
    VoidScrewHollowSky =							"Void Screw (Hollow Sky)"
    VoidScrewSomeOtherPlace =						"Void Screw (Some Other Place)"
    VoidScrewTree =									"Void Screw (Tree)"
    VoidScrewKillFish =								"Void Screw (Kill Fish)"
    VoidScrewParkTopHat =							"Void Screw (Park Top Hat)"
    VoidScrewParkOutofBounds =						"Void Screw (Park Out of Bounds)"
    VoidScrewAnxietyTower1 =						"Void Screw (Anxiety Tower #1)"
    VoidScrewAnxietyTower2 =						"Void Screw (Anxiety Tower #2)"
    THISGUYWASASICKO =								"THIS GUY WAS A SICKO!!!"
    Drill =									        "Drill"
    FallWarp =									    "Fall Warp"
    CheeseGrater =									"Cheese Grater"
    MetalWorm =									    "Metal Worm"
    HOWDY =									        "HOWDY"
    MiracleSoda1 =									"Miracle Soda #1"
    MiracleSoda2 =									"Miracle Soda #2"
    CrankAnxietyTower =								"Crank (Anxiety Tower)"
    DefeatOwlloh =                                  "Defeat Owlloh"
    TowerComplete =                                 "Tower Complete"
    AnxietyComplete =                               "Anxiety Tower Complete"
    DogGod =                                        "Dog God"
    Achievement_LittleCornCadet =                   "Little Corn Cadet"
    Achievement_XPansionPak =                       "XP-ansion Pak"
    Achievement_ImALasagnaHog   =                   "...I'm a Lasagna Hog"
    Achievement_CornSyrup =                         "Corn Syrup"
    Achievement_GetNachosOrGetOut =                 "Get N(achos) or Get Out"
    Achievement_Highdive =                          "Highdive"
    Achievement_PrivateScrew =                      "Private Screw'l"
    Achievement_SmokingKills =                      "Smoking Kills"
    Achievement_MagicalTetnisChallenge =            "Magical Tetnis Challenge"
    Achievement_HeroesInAWholeShell =               "heroes in a Whole Shell"
    Achievement_AnxietyAttack =                     "Anxiety Attack"
    Achievement_AnnoyedTheVoid =                    "Annoyed the Void"
    Achievement_MaxPower =                          "maXPower"
    Achievement_FeastFitForaKid =                   "Feast Fit For a Kid"


@dataclass
class CK64LocationData:
    name: CK64LocationName
    game_id: int
    region: Region
    # Rule lists are OR'd together.
    rules_a: List[Rule] = field(default_factory=list)
    rules_b: List[Rule] = field(default_factory=list)
    progress_type: LocationProgressType = LocationProgressType.DEFAULT


location_table: List[CK64LocationData] = [
    # region Park Cubes
    CK64LocationData(
        CK64LocationName.CubeParkNearSlide, 116,
        Region.MonsterPark,
        [Rule.Jump, Rule.WallJump_Or_Climb],
    ),
    CK64LocationData(
        CK64LocationName.CubeParkSlide, 100,
        Region.MonsterPark,
        [Rule.Climb, Rule.Jump, Rule.WallJump],
    ),
    CK64LocationData(
        CK64LocationName.CubeParkUnderSlide, 118,
        Region.MonsterPark,
        [Rule.Jump, Rule.WallJump_Or_Climb],
    ),
    CK64LocationData(
        CK64LocationName.CubeParkBouncyMoose, 113,
        Region.MonsterPark,
        [Rule.Slam],
    ),
    CK64LocationData(
        CK64LocationName.CubeParkTopHat, 106,
        Region.MonsterPark,
        [Rule.WallButton, Rule.Platforming, Rule.Slam],
    ),
    CK64LocationData(
        CK64LocationName.CubeParkAcrossWater1, 103,
        Region.MonsterParkAcrossLake,
        [Rule.Jump, Rule.WallJump_Or_Climb],
    ),
    CK64LocationData(
        CK64LocationName.CubeParkAcrossWater2, 104,
        Region.MonsterParkAcrossLake,
    ),
    CK64LocationData(
        CK64LocationName.CubeParkAcrossWater3, 119,
        Region.MonsterParkAcrossLake,
        [Rule.BombBird],
    ),
    CK64LocationData(
        CK64LocationName.CubeParkAcrossWater4, 105,
        Region.MonsterParkAcrossLake,
        [Rule.Platforming],
    ),
    CK64LocationData(
        CK64LocationName.CubeStoneStatue1, 122,
        Region.MonsterParkAcrossLake,
        [Rule.Platforming, Rule.Slam],
    ),
    CK64LocationData(
        CK64LocationName.CubeStoneStatue2, 123,
        Region.MonsterParkAcrossLake,
        [Rule.Platforming, Rule.Slam],
    ),
    CK64LocationData(
        CK64LocationName.CubeStoneStatue3, 124,
        Region.MonsterParkAcrossLake,
        [Rule.Platforming, Rule.Slam],
    ),
    CK64LocationData(
        CK64LocationName.CubeParkFence, 112,
        Region.MonsterPark,
        [Rule.Jump, Rule.WallJump],
    ),
    CK64LocationData(
        CK64LocationName.CubeParkLowerSlamPillar, 120,
        Region.MonsterPark,
        [Rule.Jump, Rule.WallJump],
    ),
    CK64LocationData(
        CK64LocationName.CubeParkUpperSlamPillar, 121,
        Region.MonsterPark,
        [Rule.Jump, Rule.WallJump, Rule.VerticalHeadbutt],
        [Rule.CanReachParkTop, Rule.Headbutt],
    ),
    CK64LocationData(
        CK64LocationName.CubeParkAtticDrill1, 126,
        Region.MonsterParkAttic,
        [Rule.BreakGroundedObject, Rule.Jump, Rule.WallJump, Rule.Drill],
    ),
    CK64LocationData(
        CK64LocationName.CubeParkAtticDrill2, 127,
        Region.MonsterParkAttic,
        [Rule.BreakGroundedObject, Rule.Jump, Rule.WallJump, Rule.Drill],
    ),
    CK64LocationData(
        CK64LocationName.CubeParkAtticHigh1, 128,
        Region.MonsterParkAttic,
        [Rule.BreakGroundedObject, Rule.Platforming, Rule.Drill],
    ),
    CK64LocationData(
        CK64LocationName.CubeParkAtticHigh2, 130,
        Region.MonsterParkAttic,
        [Rule.BreakGroundedObject, Rule.Platforming, Rule.Drill],
    ),
    CK64LocationData(
        CK64LocationName.CubeParkAtticHallway, 129,
        Region.MonsterParkAttic,
        [Rule.BreakGroundedObject, Rule.Platforming],
    ),
    CK64LocationData(
        CK64LocationName.CubeParkHouseBookcase, 117,
        Region.MonsterParkHouse,
    ),
    CK64LocationData(
        CK64LocationName.CubeParkHouseFoyer1, 107,
        Region.MonsterParkHouseFoyer,
        [Rule.Jump, Rule.Headbutt, Rule.WallJump_Or_Climb],
    ),
    CK64LocationData(
        CK64LocationName.CubeParkHouseFoyer2, 115,
        Region.MonsterParkHouseFoyer,
        [Rule.Jump, Rule.Headbutt, Rule.WallJump_Or_Climb],
    ),
    CK64LocationData(
        CK64LocationName.CubeParkHouseFoyer3, 114,
        Region.MonsterParkHouseFoyer,
        [Rule.MaxPlatforming],
        [Rule.CanReachParkTop, Rule.Climb],
    ),
    CK64LocationData(
        CK64LocationName.CubeParkHouseFoyerTower, 131,
        Region.MonsterParkHouseFoyer,
        [Rule.MaxPlatforming],
        [Rule.CanReachParkTop, Rule.Jump_Or_Headbutt],
    ),
    CK64LocationData(
        CK64LocationName.CubeParkTopBouncyMoose, 125,
        Region.MonsterParkTop,
        [Rule.Slam, Rule.Headbutt, Rule.WallJump],
    ),
    CK64LocationData(
        CK64LocationName.CubeParkTopButtonChallenge1, 109,
        Region.MonsterParkTop,
        [Rule.Platforming, Rule.Headbutt],
    ),
    CK64LocationData(
        CK64LocationName.CubeParkTopButtonChallenge2, 110,
        Region.MonsterParkTop,
        [Rule.Platforming, Rule.Headbutt],
    ),
    CK64LocationData(
        CK64LocationName.CubeParkTopButtonChallenge3, 111,
        Region.MonsterParkTop,
        [Rule.Platforming, Rule.Headbutt],
    ),
    CK64LocationData(
        CK64LocationName.CubeParkDrillPastLake, 108,
        Region.MonsterParkAcrossLake,
        [Rule.DrillDownwards],
    ),
    # endregion
    # region Park Screws
    CK64LocationData(
        CK64LocationName.ScrewParkLakeBombYeet, 135,
        Region.MonsterParkAcrossLake,
        [Rule.BombBird, Rule.Slam, Rule.Swim],
    ),
    CK64LocationData(
        CK64LocationName.ScrewParkAtticScrewScrew, 137,
        Region.MonsterParkAttic,
        [Rule.BreakGroundedObject, Rule.Jump, Rule.Headbutt, Rule.WallJump],
    ),
    CK64LocationData(
        CK64LocationName.ScrewParkAtticDrill, 136,
        Region.MonsterParkAttic,
        [Rule.BreakGroundedObject, Rule.Platforming, Rule.Headbutt, Rule.Drill],
    ),
    CK64LocationData(
        CK64LocationName.ScrewParkAboveCrank, 134,
        Region.MonsterParkAcrossLake,
        [Rule.Platforming, Rule.Slam, Rule.Headbutt],
        [Rule.CanReachParkTop, Rule.Headbutt],
    ),
    CK64LocationData(
        CK64LocationName.ScrewParkHouseFoyer, 138,
        Region.MonsterParkHouseFoyer,
        [Rule.Jump, Rule.WallJump, Rule.Headbutt],
    ),
    CK64LocationData(
        CK64LocationName.ScrewParkTopWallJumpChallenge, 133,
        Region.MonsterParkTop,
        [Rule.Jump, Rule.Slam, Rule.WallJump, Rule.WallJump_Or_Climb, Rule.Headbutt],
    ),
    # endregion
    # region Park Chameleons
    CK64LocationData(
        CK64LocationName.ChameleonPark, 139,
        Region.MonsterPark,
        [Rule.Chameleon],
    ),
    CK64LocationData(
        CK64LocationName.ChameleonInterior, 140,
        Region.MonsterParkHouse,
        [Rule.Chameleon],
    ),
    # endregion
    # region Park Crystals
    CK64LocationData(
        CK64LocationName.CrystalParkAttic, 143,
        Region.MonsterParkAttic,
        [Rule.Jump, Rule.WallJump, Rule.BreakCrystal],
    ),
    CK64LocationData(
        CK64LocationName.CrystalGarbageGrump, 144,
        Region.MonsterParkSewers,
        [Rule.AllTrashcans, Rule.BreakGroundedObject],
    ),
    # endregion
    # region Park Mirrors
    CK64LocationData(
        CK64LocationName.MirrorParkSewers, 142,
        Region.MonsterParkSewers,
        [Rule.Platforming, Rule.Headbutt],
    ),
    CK64LocationData(
        CK64LocationName.MirrorFoyerLevel3, 141,
        Region.MonsterParkHouseFoyer,
        [Rule.Level3, Rule.Slam, Rule.Headbutt, Rule.Jump, Rule.WallJump_Or_Climb],
    ),
    # endregion
    # region Park Cranks
    CK64LocationData(
        CK64LocationName.CrankMonsterParkAcrossLake, 132,
        Region.MonsterParkAcrossLake,
        [Rule.OpenChest, Rule.Platforming],
    ),
    # endregion
    # region Trash Cans
    CK64LocationData(
        CK64LocationName.TrashCanPark, 152,
        Region.MonsterPark,
        [Rule.BreakTrashcan],
    ),
    CK64LocationData(
        CK64LocationName.TrashCanAttic1, 153,
        Region.MonsterParkAttic,
        [Rule.Jump, Rule.WallJump, Rule.Headbutt, Rule.BreakTrashcan],
    ),
    CK64LocationData(
        CK64LocationName.TrashCanAttic2, 151,
        Region.MonsterParkAttic,
        [Rule.Platforming, Rule.BreakTrashcan],
    ),
    CK64LocationData(
        CK64LocationName.TrashCanSewers, 148,
        Region.MonsterParkSewers,
        [Rule.Jump, Rule.WallJump, Rule.BreakTrashcan],
    ),
    CK64LocationData(
        CK64LocationName.TrashCanFoyer, 155,
        Region.MonsterParkHouseFoyer,
        [Rule.Jump, Rule.Headbutt, Rule.WallJump_Or_Climb, Rule.BreakTrashcan],
    ),
    CK64LocationData(
        CK64LocationName.TrashCanParkTop, 150,
        Region.MonsterParkTop,
        [Rule.CanReachParkTop, Rule.BreakTrashcan],
    ),
    CK64LocationData(
        CK64LocationName.TrashCanParkTopWallJumpChallenge, 149,
        Region.MonsterParkTop,
        [Rule.Jump, Rule.Slam, Rule.WallJump, Rule.WallJump_Or_Climb, Rule.BreakTrashcan],
    ),
    CK64LocationData(
        CK64LocationName.TrashCanFoyerLevel3, 154,
        Region.MonsterParkHouseFoyer,
        [Rule.Level3, Rule.BreakTrashcan],
    ),
    # endregion
    # region Hollow Cubes
    CK64LocationData(
        CK64LocationName.CubeHollowBridge1, 254,
        Region.WollowsHollow,
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowBridge2, 275,
        Region.WollowsHollow,
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowBridge3, 276,
        Region.WollowsHollow,
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowOnTrees, 209,
        Region.WollowsHollow,
        [Rule.Jump, Rule.Slam],
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowLeavesUnderOwlTree, 225,
        Region.WollowsHollow,
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowLeavesOnOwlTree, 226,
        Region.WollowsHollow,
        [Rule.Jump],
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowPillar1, 216,
        Region.WollowsHollow,
        [Rule.Jump, Rule.WallJump],
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowPillar2, 217,
        Region.WollowsHollow,
        [Rule.Jump, Rule.WallJump, Rule.Headbutt],
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowTrampoline, 266,
        Region.WollowsHollow,
        [Rule.Slam],
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowTrinketShop, 232,
        Region.WollowsHollow,
        [Rule.MaxPlatforming],
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowClockWallClimb1, 231,
        Region.WollowsHollow,
        [Rule.Platforming],
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowClockWallClimb2, 230,
        Region.WollowsHollow,
        [Rule.MaxPlatforming],
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowPillarOutsideChurch, 224,
        Region.WollowsHollow,
        [Rule.Jump, Rule.Climb_Or_Headbutt, Rule.WallJump],
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowClockwiseVomit, 265,
        Region.WollowsHollow,
        [Rule.Jump, Rule.Slam],
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowFartTunnel1, 215,
        Region.WollowsHollow,
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowFartTunnel2, 214,
        Region.WollowsHollow,
        [Rule.Jump, Rule.WallJump],
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowChurch1, 233,
        Region.WollowsHollowChurch,
        [Rule.Jump, Rule.Climb, Rule.WallJump_Or_Headbutt],
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowChurch2, 255,
        Region.WollowsHollowChurch,
        [Rule.MaxPlatforming],
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowChurch3, 271,
        Region.WollowsHollowChurch,
        [Rule.MaxPlatforming],
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowGraveyardPole1, 273,
        Region.WollowsHollowGraveyard,
        [Rule.Climb],
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowGraveyardTacoCat, 261,
        Region.WollowsHollowGraveyard,
        [Rule.Platforming],
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowGraveyardPole2, 274,
        Region.WollowsHollowGraveyard,
        [Rule.Climb],
        [Rule.CanReachGraveyardTop],
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowGraveyardBehindWetTree, 253,
        Region.WollowsHollowGraveyard,
        [Rule.Platforming],
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowGraveyardWater, 256,
        Region.WollowsHollowGraveyard,
        [Rule.Swim],
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowGraveyardTombstoneCode1, 262,
        Region.WollowsHollowGraveyard,
        [Rule.BreakGroundedObject],
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowGraveyardTombstoneCode2, 263,
        Region.WollowsHollowGraveyard,
        [Rule.BreakGroundedObject],
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowGraveyardTombstoneCode3, 264,
        Region.WollowsHollowGraveyard,
        [Rule.BreakGroundedObject],
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowBalcony1, 210,
        Region.WollowsHollow,
        [Rule.Jump, Rule.Climb, Rule.Headbutt],
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowBalcony2, 211,
        Region.WollowsHollow,
        [Rule.Jump, Rule.Climb, Rule.Headbutt],
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowNearBats1, 218,
        Region.WollowsHollowCagedRooftops,
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowNearBats2, 219,
        Region.WollowsHollowCagedRooftops,
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowDrillRoom1, 242,
        Region.WollowsHollowDrillChamber,
        [Rule.DrillDownwards],
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowDrillRoom2, 244,
        Region.WollowsHollowGraveyard,
        [Rule.DrillDownwards],
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowDrillRoom3, 246,
        Region.WollowsHollowGraveyard,
        [Rule.DrillDownwards],
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowDrillUnderRamp, 248,
        Region.WollowsHollow,
        [Rule.DrillMinimal],
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowDrillBars1, 220,
        Region.WollowsHollow,
        [Rule.DrillMinimal],
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowDrillBars2, 221,
        Region.WollowsHollow,
        [Rule.DrillMinimal],
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowDrillUnderChurch1, 236,
        Region.WollowsHollow,
        [Rule.DrillMinimal],
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowDrillUnderChurch2, 238,
        Region.WollowsHollow,
        [Rule.DrillMinimal],
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowDrillDragonMountainside1, 212,
        Region.WollowsHollow,
        [Rule.CanReachGraveyard, Rule.Slam, Rule.Drill],
        [Rule.DragonPlatforming, Rule.Drill],
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowDrillDragonMountainside2, 213,
        Region.WollowsHollow,
        [Rule.CanReachGraveyard, Rule.Slam, Rule.Drill],
        [Rule.DragonPlatforming, Rule.Drill],
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowHauntedHouseTop1, 222,
        Region.WollowsHollow,
        [Rule.DragonPlatforming],
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowHauntedHouseTop2, 223,
        Region.WollowsHollow,
        [Rule.DragonPlatforming],
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowHauntedHouseBehindChimney, 272,
        Region.WollowsHollowHouseTop,
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowRavine1, 229,
        Region.WollowsHollowRavine,
        [Rule.Jump, Rule.WallJump, Rule.Climb_Or_Headbutt],
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowRavine2, 227,
        Region.WollowsHollowRavine,
        [Rule.Platforming],
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowRavine3, 228,
        Region.WollowsHollowRavine,
        [Rule.Platforming],
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowFencedAcrossRavine, 277,
        Region.WollowsHollowRavine,
        [Rule.MaxPlatforming],
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowMusicBoxSwim1, 278,
        Region.WollowsHollowMusic,
        [Rule.Swim],
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowMusicBoxSwim2, 279,
        Region.WollowsHollowMusic,
        [Rule.Swim],
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowBrickWall1, 234,
        Region.WollowsHollow,
        [Rule.Jump, Rule.Headbutt, Rule.Slam, Rule.Climb_Or_Headbutt],
        [Rule.CanReachCagedRooftops, Rule.CanGetHurt],
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowBrickWall2, 235,
        Region.WollowsHollowMusic,
        [Rule.Jump, Rule.Headbutt, Rule.Slam, Rule.Climb_Or_Headbutt],
        [Rule.CanReachCagedRooftops, Rule.CanGetHurt],
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowBehindSanitaryZoo, 240,
        Region.WollowsHollowZooOutside,
        [Rule.DrillDownwards],
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowSpiderOutsideZoo, 252,
        Region.WollowsHollowZooOutside,
        [Rule.Jump, Rule.Headbutt, Rule.Climb],
    ),
    CK64LocationData(
        CK64LocationName.CubeFlippedHollowDragonCrankDrill, 250,
        Region.WollowsHollowTreeSideRoom,
        [Rule.BatTreeSideRoomCollectables],
    ),
    CK64LocationData(
        CK64LocationName.CubeFlippedHollowFountainSwim1, 267,
        Region.WollowsHollow,
        [Rule.CanEnterFountain],
    ),
    CK64LocationData(
        CK64LocationName.CubeFlippedHollowFountainSwim2, 268,
        Region.WollowsHollow,
        [Rule.CanEnterFountain],
    ),
    CK64LocationData(
        CK64LocationName.CubeFlippedHollowFountainSwim3, 269,
        Region.WollowsHollow,
        [Rule.CanEnterFountain],
    ),
    CK64LocationData(
        CK64LocationName.CubeFlippedHollowFountainSwim4, 270,
        Region.WollowsHollow,
        [Rule.CanEnterFountain],
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowTreeFishTimer, 257,
        Region.WollowsHollowTree,
        [Rule.Jump, Rule.Headbutt, Rule.Swim],
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowTreeSwim, 259,
        Region.WollowsHollowTree,
        [Rule.Swim],
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowTreeNearMetalWorm, 258,
        Region.WollowsHollowTree,
        [Rule.CanClimbInteriorTree],
    ),
    CK64LocationData(
        CK64LocationName.CubeHollowGraveyardSpiderCaveDrill, 260,
        Region.WollowsHollowGraveyard,
        [Rule.Swim, Rule.BombBird, Rule.Platforming, Rule.Slam, Rule.Drill],
    ),
    # endregion
    # region Hollow Screws
    CK64LocationData(
        CK64LocationName.ScrewHollowTownClock, 203,
        Region.WollowsHollow,
        [Rule.MaxPlatforming, Rule.Headbutt],
    ),
    CK64LocationData(
        CK64LocationName.ScrewHollowDrillTowerAlcove, 200,
        Region.WollowsHollowCagedRooftops,
    ),
    CK64LocationData(
        CK64LocationName.ScrewHollowBehindHauntedHouse, 202,
        Region.WollowsHollowGraveyard,
        [Rule.Jump, Rule.Headbutt],
    ),
    CK64LocationData(
        CK64LocationName.ScrewHollowDragonCave, 208,
        Region.WollowsHollowCave,
        [Rule.Slam],
    ),
    CK64LocationData(
        CK64LocationName.ScrewHollowLargeCrankPit, 201,
        Region.WollowsHollow,
        [Rule.Jump, Rule.Headbutt],
    ),
    CK64LocationData(
        CK64LocationName.ScrewHollowZoo, 207,
        Region.WollowsHollowZoo,
        [Rule.MaxPlatforming, Rule.Drill],
    ),
    CK64LocationData(
        CK64LocationName.ScrewFlippedHollowTreeSideRoom, 204,
        Region.WollowsHollow,
        [Rule.BatTreeSideRoomCollectables],
    ),
    CK64LocationData(
        CK64LocationName.ScrewHollowTreeHighScrew, 205,
        Region.WollowsHollowTree,
        [Rule.MaxPlatforming, Rule.BatTreeSideRoomCollectables],
    ),
    CK64LocationData(
        CK64LocationName.ScrewHollowTreeLowScrew, 206,
        Region.WollowsHollowTree,
        [Rule.MaxPlatforming],
    ),
    # endregion
    # region Hollow Chameleons
    CK64LocationData(
        CK64LocationName.ChameleonHollowBush, 297,
        Region.WollowsHollow,
        [Rule.Chameleon],
    ),
    CK64LocationData(
        CK64LocationName.ChameleonHollowGraveyard, 296,
        Region.WollowsHollowGraveyard,
        [Rule.Chameleon],
    ),
    # endregion
    # region Hollow Crystals
    CK64LocationData(
        CK64LocationName.CrystalHollowTimedFountain, 283,
        Region.WollowsHollow,
        [Rule.Jump, Rule.WallJump_Or_Climb, Rule.Headbutt],
    ),
    CK64LocationData(
        CK64LocationName.CrystalHollowChurchBell, 282,
        Region.WollowsHollowChurchTop,
        [Rule.MaxPlatforming],
    ),
    CK64LocationData(
        CK64LocationName.CrystalHollowGraveyardSpiderReward, 291,
        Region.WollowsHollowGraveyard,
        [Rule.CheeseGrater],
    ),
    CK64LocationData(
        CK64LocationName.CrystalHollowDrillPillar, 286,
        Region.WollowsHollow,
        [Rule.MaxPlatforming, Rule.DrillDownwards],
        [Rule.CanReachRooftops, Rule.DrillDownwards, Rule.Headbutt],
    ),
    CK64LocationData(
        CK64LocationName.CrystalHollowHauntedHouseFreeBird, 285,
        Region.WollowsHollowHouse,
        [Rule.Jump, Rule.Headbutt, Rule.CanFreeHauntedHouseBird],
    ),
    CK64LocationData(
        CK64LocationName.CrystalHollowDragonCave, 295,
        Region.WollowsHollowCave,
        [Rule.Jump, Rule.Headbutt, Rule.WallJump, Rule.Slam],
    ),
    CK64LocationData(
        CK64LocationName.CrystalHollowAboveEntry, 280,
        Region.WollowsHollowRavine,
        [Rule.MaxPlatforming],
    ),
    CK64LocationData(
        CK64LocationName.CrystalHollowZombieChamber, 292,
        Region.WollowsHollowZombies,
        [Rule.MaxPlatforming, Rule.CanBeatZombieTurtle, Rule.Drill],
    ),
    CK64LocationData(
        CK64LocationName.CrystalHollowFreeStuckPig, 294,
        Region.WollowsHollow,
        [Rule.Jump, Rule.Headbutt],
    ),
    CK64LocationData(
        CK64LocationName.CrystalHollowBombChurchPillar, 281,
        Region.WollowsHollow,
        [Rule.Jump, Rule.Headbutt],
    ),
    CK64LocationData(
        CK64LocationName.CrystalFlippedHollowCounterclockwiseVomit, 293,
        Region.WollowsHollow,
        [Rule.Jump, Rule.Slam, Rule.CanReachFlippedHollow],
    ),
    CK64LocationData(
        CK64LocationName.CrystalFlippedHollowGassyMoosey, 287,
        Region.WollowsHollowTrinkets,
        [Rule.MaxPlatforming, Rule.CanReachFlippedHollow],
    ),
    # endregion
    # region Hollow Mirrors
    CK64LocationData(
        CK64LocationName.MirrorHollowGraveyard, 289,
        Region.WollowsHollowAboveGraveyard,
        [Rule.Jump, Rule.Headbutt, Rule.Climb, Rule.Slam],
    ),
    CK64LocationData(
        CK64LocationName.MirrorHollowZooSideCrank, 284,
        Region.WollowsHollow,
        [Rule.CrankZooSide, Rule.MaxPlatforming, Rule.Drill, Rule.Crouch],
    ),
    CK64LocationData(
        CK64LocationName.MirrorFlippedHollowDragonCrank, 288,
        Region.WollowsHollow,
        [Rule.CanReachFlippedHollow, Rule.Jump, Rule.Headbutt, Rule.CrankHollowDragonWall, Rule.Climb],
    ),
    CK64LocationData(
        CK64LocationName.MirrorZooMetalWorm, 290,
        Region.WollowsHollowZoo,
        [Rule.CanUseMetalWorm],
    ),
    # endregion
    # region Hollow Cranks
    CK64LocationData(
        CK64LocationName.CrankHollowHauntedHouseGroundFloor, 198,
        Region.WollowsHollowGraveyard,
        [Rule.Level2, Rule.Jump, Rule.Headbutt],
    ),
    CK64LocationData(
        CK64LocationName.CrankHollowRavine, 298,
        Region.WollowsHollowRavine,
        [Rule.Platforming],
    ),
    # endregion
    # region Disco Balls
    CK64LocationData(
        CK64LocationName.DiscoBallHollowTrinketShop, 319,
        Region.WollowsHollow,
        [Rule.MaxPlatforming],
    ),
    CK64LocationData(
        CK64LocationName.DiscoBallHollowDragonChest, 300,
        Region.WollowsHollow,
        [Rule.DragonPlatforming, Rule.Headbutt, Rule.Drill],
    ),
    CK64LocationData(
        CK64LocationName.DiscoBallHollowMusicBox, 308,
        Region.WollowsHollowMusic,
        [Rule.MaxPlatforming],
    ),
    CK64LocationData(
        CK64LocationName.DiscoBallHollowZombieChamber, 302,
        Region.WollowsHollowZombies,
        [Rule.CanBeatZombieTurtle, Rule.Jump, Rule.Headbutt],
    ),
    CK64LocationData(
        CK64LocationName.DiscoBallHollowCleanZoo, 304,
        Region.WollowsHollowZoo,
        [Rule.CanCleanZoo],
    ),
    # endregion
    # region Bottlecaps
    CK64LocationData(
        CK64LocationName.BottleCapHollowGraveyard, 306,
        Region.WollowsHollowGraveyard,
        [Rule.MaxPlatforming],
    ),
    CK64LocationData(
        CK64LocationName.BottleCapHollowGraveyardInsideWetTree, 317,
        Region.WollowsHollowGraveyard,
        [Rule.Swim, Rule.Jump, Rule.WallJump, Rule.Climb],
    ),
    CK64LocationData(
        CK64LocationName.BottleCapHollowRavineClimb, 311,
        Region.WollowsHollowRavine,
        [Rule.MaxPlatforming],
    ),
    CK64LocationData(
        CK64LocationName.BottleCapHollowZooRooftop, 313,
        Region.WollowsHollowZooOutside,
        [Rule.DrillDownwards, Rule.Slam, Rule.Climb],
    ),
    CK64LocationData(
        CK64LocationName.BottleCapHollowZooSideCrank, 315,
        Region.WollowsHollow,
        [Rule.CrankZooSide],
    ),
    # endregion
    # region Void Screws
    CK64LocationData(
        CK64LocationName.VoidScrewParkHouse, 146,
        Region.MonsterParkHouse,
        [Rule.Jump, Rule.WallJump_Or_Climb, Rule.VerticalHeadbutt],
    ),
    CK64LocationData(
        CK64LocationName.VoidScrewHollowOutsideTrinketShop, 324,
        Region.WollowsHollow,
        [Rule.MaxPlatforming],
    ),
    CK64LocationData(
        CK64LocationName.VoidScrewHollowChurch, 321,
        Region.WollowsHollowChurch,
        [Rule.MaxPlatforming],
    ),
    CK64LocationData(
        CK64LocationName.VoidScrewHollowSky, 323,
        Region.WollowsHollowCagedRooftops,
    ),
    CK64LocationData(
        CK64LocationName.VoidScrewSomeOtherPlace, 501,
        Region.SomeOtherPlace,
    ),
    CK64LocationData(
        CK64LocationName.VoidScrewTree, 322,
        Region.WollowsHollowTree,
        [Rule.MaxPlatforming, Rule.PostOwllohDefeated],
    ),
    CK64LocationData(
        CK64LocationName.VoidScrewKillFish, 325,
        Region.WollowsHollowZombies,
        [Rule.CanClimbInteriorTree, Rule.CanAccessGraveyardBomb],
    ),
    CK64LocationData(
        CK64LocationName.VoidScrewParkTopHat, 145,
        Region.MonsterPark,
        [Rule.MaxPlatforming, Rule.Drill, Rule.Slam],
    ),
    CK64LocationData(
        CK64LocationName.VoidScrewParkOutofBounds, 147,
        Region.MonsterPark,
        [Rule.MaxPlatforming, Rule.DrillDownwards, Rule.CanReachAttic],
    ),
    CK64LocationData(
        CK64LocationName.VoidScrewAnxietyTower1, 411,
        Region.AnxietyTower,
        [Rule.AnxietyTowerChecks, Rule.Slam],
    ),
    CK64LocationData(
        CK64LocationName.VoidScrewAnxietyTower2, 412,
        Region.AnxietyTower,
        [Rule.AnxietyTowerChecks, Rule.Slam, Rule.Crouch],
    ),
    # endregion
    # region Anxiety Tower
    CK64LocationData(
        CK64LocationName.CrankAnxietyTower, 414,
        Region.AnxietyTower,
        [Rule.MaxPlatforming],
    ),
    # endregion
    # region Upgrades
    CK64LocationData(
        CK64LocationName.MiracleSoda1, 326,
        Region.WollowsHollow,
        [Rule.AllBottlecaps],
    ),
    CK64LocationData(
        CK64LocationName.MiracleSoda2, 500,
        Region.SomeOtherPlace,
        [Rule.AtLeastFourVoidScrews, Rule.MaxPlatforming],
        [],
        LocationProgressType.EXCLUDED,
    ),
    CK64LocationData(
        CK64LocationName.Drill, 2001,
        Region.WollowsHollowDrillChamber,
        [Rule.Jump, Rule.Climb],
    ),
    CK64LocationData(
        CK64LocationName.FallWarp, 2002,
        Region.WollowsHollowChurch,
        [Rule.MaxPlatforming],
    ),
    # endregion
    # region Misc Quest
    CK64LocationData(
        CK64LocationName.CheeseGrater, 310,
        Region.WollowsHollowGraveyard,
        [Rule.CanAccessGraveyardBomb, Rule.Slam],
    ),
    CK64LocationData(
        CK64LocationName.MetalWorm, 2003,
        Region.WollowsHollowTree,
        [Rule.CanClimbInteriorTree],
    ),
    # endregion
    # region Silly
    CK64LocationData(
        CK64LocationName.THISGUYWASASICKO, 2000,
        Region.WollowsHollowHouseTop,
        [Rule.Jump, Rule.Slam],
    ),
    CK64LocationData(
        CK64LocationName.HOWDY, 2004,
        Region.WollowsHollowZoo,
        [Rule.CanUseMetalWorm],
    ),
    # endregion
    # region Completion
    CK64LocationData(
        CK64LocationName.DefeatOwlloh, 3000,
        Region.WollowsHollowTree,
        [Rule.CanDefeatOwlloh]
    ),
    CK64LocationData(
        CK64LocationName.TowerComplete, 3001,
        Region.Tower,
        [Rule.PostOwllohDefeated, Rule.TowerMovement]
    ),
    CK64LocationData(
        CK64LocationName.AnxietyComplete, 3002,
        Region.AnxietyTower,
        [Rule.PostOwllohDefeated, Rule.TowerMovement]
    ),
    CK64LocationData(
        CK64LocationName.DogGod, 3003,
        Region.SomeOtherPlace,
        [Rule.AllVoidScrews, Rule.TowerMovement, Rule.Swim]
    ),
    # endregion
    # region Achievements
    CK64LocationData(
        CK64LocationName.Achievement_LittleCornCadet, 4000,
        Region.MonsterParkTop,
    ),
    CK64LocationData(
        CK64LocationName.Achievement_XPansionPak, 4001,
        Region.Menu,
        [Rule.Level2],
    ),
    CK64LocationData(
        CK64LocationName.Achievement_ImALasagnaHog, 4002,
        Region.WollowsHollow,
        [Rule.PostOwllohDefeated],
    ),
    CK64LocationData(
        CK64LocationName.Achievement_CornSyrup, 4003,
        Region.WollowsHollow,
        [Rule.AnyHPItem],
    ),
    CK64LocationData(
        CK64LocationName.Achievement_GetNachosOrGetOut, 4004,
        Region.Tower,
        [Rule.TowerMovement],
    ),
    CK64LocationData(
        CK64LocationName.Achievement_Highdive, 4005,
        Region.WollowsHollowTree,
        [Rule.CanClimbInteriorTree],
    ),
    CK64LocationData(
        CK64LocationName.Achievement_PrivateScrew, 4006,
        Region.Menu,
        [Rule.AnyVoidScrew],
    ),
    CK64LocationData(
        CK64LocationName.Achievement_SmokingKills, 4007,
        Region.MonsterPark,
        [Rule.BreakGroundedObject, Rule.Jump, Rule.WallJump_Or_Climb],
    ),
    CK64LocationData(
        CK64LocationName.Achievement_MagicalTetnisChallenge, 4008,
        Region.MonsterPark,
        [Rule.DrillDownwards],
    ),
    CK64LocationData(
        CK64LocationName.Achievement_HeroesInAWholeShell, 4009,
        Region.WollowsHollow,
        [Rule.Jump, Rule.Headbutt, Rule.BombBird],
    ),
    CK64LocationData(
        CK64LocationName.Achievement_AnxietyAttack, 4010,
        Region.AnxietyTower,
        [Rule.AnxietyTowerChecks, Rule.TowerMovement],
    ),
    CK64LocationData(
        CK64LocationName.Achievement_AnnoyedTheVoid, 4011,
        Region.SomeOtherPlace,
        [Rule.AtLeastFourVoidScrews],
    ),
    CK64LocationData(
        CK64LocationName.Achievement_MaxPower, 4012,
        Region.Menu,
        [Rule.Level6],
    ),
    CK64LocationData(
        CK64LocationName.Achievement_FeastFitForaKid, 4013,
        Region.AnxietyTower,
        [Rule.Jump, Rule.Headbutt],
    ),
    # endregion
]


locked_locations = [
    CK64LocationName.DefeatOwlloh,
    CK64LocationName.TowerComplete,
    CK64LocationName.AnxietyComplete,
    CK64LocationName.DogGod,
]

goal_locations = {
    Goal.option_owlloh: CK64LocationName.DefeatOwlloh,
    Goal.option_tower: CK64LocationName.TowerComplete,
    Goal.option_anxiety: CK64LocationName.AnxietyComplete,
    Goal.option_god: CK64LocationName.DogGod,
}

achievement_locations = [
    CK64LocationName.Achievement_LittleCornCadet,
    CK64LocationName.Achievement_XPansionPak,
    CK64LocationName.Achievement_ImALasagnaHog,
    CK64LocationName.Achievement_CornSyrup,
    CK64LocationName.Achievement_GetNachosOrGetOut,
    CK64LocationName.Achievement_Highdive,
    CK64LocationName.Achievement_PrivateScrew,
    CK64LocationName.Achievement_SmokingKills,
    CK64LocationName.Achievement_MagicalTetnisChallenge,
    CK64LocationName.Achievement_HeroesInAWholeShell,
    CK64LocationName.Achievement_AnxietyAttack,
    CK64LocationName.Achievement_AnnoyedTheVoid,
    CK64LocationName.Achievement_MaxPower,
    CK64LocationName.Achievement_FeastFitForaKid,
]


def validate_locations() -> bool:
    dupes = set()
    for loc in location_table:
        if loc.game_id in dupes:
            return False
        dupes.add(loc.game_id)
    return True
