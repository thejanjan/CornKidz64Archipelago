from dataclasses import dataclass

from Options import Choice, Range, Toggle, DefaultOnToggle, DeathLink, PerGameCommonOptions


class Goal(Choice):
    """The clear condition to finish the game."""
    display_name = "goal"
    option_owlloh = 0
    option_tower = 1
    option_anxiety = 2
    option_god = 3
    default = 0


class GoatColor(Choice):
    """The color for Seve."""
    display_name = "goat_color"
    option_red = 0
    option_green = 1
    option_blue = 2
    default = 0


class XPCount(Range):
    """The amount of XP items in the item pool."""
    display_name = "xp_count"
    range_start = 1
    range_end = 360
    default = 72


class MaxHP(Range):
    """Seve's starting max HP.
    Adds max HP items into the item pool."""
    display_name = "max_hp"
    range_start = 1
    range_end = 8
    default = 8


class Cranksanity(Toggle):
    """Randomizes the locations where cranks can be found."""
    display_name = "cranksanity"


class Ratsanity(Toggle):
    """Adds the Sanitary Zoo rats into the item pool.
    Collecting them all is required for the zoo to be clean."""
    display_name = "ratsanity"


class Achievements(Toggle):
    """Adds achievements into the item pool."""
    display_name = "achievements"


class TrapPercentage(Range):
    """Determines the number of trap items when populating the item pool with filler."""
    display_name = "trap_percentage"
    range_start = 0
    range_end = 100
    default = 25


class CanJump(DefaultOnToggle):
    """Determines if Seve can jump by default."""
    display_name = "can_jump"


class CanPunch(DefaultOnToggle):
    """Determines if Seve can punch by default."""
    display_name = "can_punch"


class CanClimb(DefaultOnToggle):
    """Determines if Seve can climb ledges or pipes by default."""
    display_name = "can_climb"


class CanGroundPound(DefaultOnToggle):
    """Determines if Seve can ground pound by default."""
    display_name = "can_ground_pound"


class CanHeadbutt(DefaultOnToggle):
    """Determines if Seve can headbutt by default."""
    display_name = "can_headbutt"


class CanWallJump(DefaultOnToggle):
    """Determines if Seve can wall jump by default."""
    display_name = "can_wall_jump"


class CanSwim(DefaultOnToggle):
    """Determines if Seve can swim underwater by default."""
    display_name = "can_swim"


class CanCrouch(DefaultOnToggle):
    """Determines if Seve can crouch by default."""
    display_name = "can_crouch"


class CanDrill(Toggle):
    """Determines if Seve can drill into terrain by default."""
    display_name = "can_drill"


class CanFallWarp(DefaultOnToggle):
    """Determines if Seve can fall warp by default."""
    display_name = "can_fall_warp"


class CornKidz64DeathLink(DeathLink):
    """When you die, everyone dies. The reverse is also true."""


@dataclass
class CornKidz64GameOptions(PerGameCommonOptions):
    goal: Goal
    goat_color: GoatColor
    xp_count: XPCount
    max_hp: MaxHP
    cranksanity: Cranksanity
    ratsanity: Ratsanity
    achievements: Achievements
    trap_percentage: TrapPercentage
    can_jump: CanJump
    can_punch: CanPunch
    can_climb: CanClimb
    can_ground_pound: CanGroundPound
    can_headbutt: CanHeadbutt
    can_wall_jump: CanWallJump
    can_swim: CanSwim
    can_crouch: CanCrouch
    can_drill: CanDrill
    can_fall_warp: CanFallWarp
    death_link: DeathLink
