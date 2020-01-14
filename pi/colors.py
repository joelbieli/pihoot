import enum

class Colors(enum.Enum):
  BLUE = 1
  RED = 2
  YELLOW = 3
  GREEN = 4

class RGBColors(enum.Enum):
  BLACK = 1
  RED = 2
  GREEN = 3
  BLUE = 4
  LIGHTBLUE = 5
  YELLOW = 6
  PURPLE = 7

RGB_COLORS = {
  RGBColors.BLACK: (0, 0, 0),
  RGBColors.RED: (1, 0, 0),
  RGBColors.GREEN: (0, 1, 0),
  RGBColors.BLUE: (0, 0, 1),
  RGBColors.LIGHTBLUE: (0, 1, 1),
  RGBColors.YELLOW: (1, 1, 0),
  RGBColors.PURPLE: (1, 0, 1)
}
