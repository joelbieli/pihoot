import enum

'''
The game state redulates the behaviour of the other submanagers
and the main event loop.
'''
class GameState(enum.Enum):
  # Intro at the beginning
  STARTING = 1
  # Trying to connect to the server
  CONNECTING = 2
  # Waiting for games
  WAITING_GAMES = 3
  # Waiting for question
  WAITING_QUESTION = 4
  # Redular answer input
  INPUT_REGULAR = 5
  # Input for Color Code
  INPUT_COLORCODE = 6
  # Error
  ERROR = 7
  # Reset game
  RESET = 8
