import enum

'''
Colors that are used for button inputs and LED outputs
aswell as Network transfers of questions
'''
class Colors(enum.Enum):
  BLUE = 1
  RED = 2
  YELLOW = 3
  GREEN = 4

'''
Colors that are used fir the RGB LED
'''
class RGBColors(enum.Enum):
  BLACK = 1
  RED = 2
  GREEN = 3
  BLUE = 4
  LIGHTBLUE = 5
  YELLOW = 6
  PURPLE = 7

'''
This map maps the Colors to actual RGB tuples that are used in the
LED manager
'''
RGB_COLORS = {
  RGBColors.BLACK: (0, 0, 0),
  RGBColors.RED: (1, 0, 0),
  RGBColors.GREEN: (0, 1, 0),
  RGBColors.BLUE: (0, 0, 1),
  RGBColors.LIGHTBLUE: (0, 1, 1),
  RGBColors.YELLOW: (1, 1, 0),
  RGBColors.PURPLE: (1, 0, 1)
}
