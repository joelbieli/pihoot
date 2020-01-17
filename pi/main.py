import gpiozero
import time
import logging
import enum
import os

import animator

from colors import Colors
from colors import RGBColors
from buttonmanager import GPIOButtonManager
from ledmanager import GPIOLEDManager
from network import NetworkManager

class GameManager(object):
  def __init__(self):
    self.state = GameState.STARTING
    self.leds = GPIOLEDManager()
    self.buttons = GPIOButtonManager()
    self.network = NetworkManager("10.0.0.10", 8080, self)
    self.game_list = []
    self.active_game = None
    self._animator = animator.Animator(self.leds, self)
    
    # Try to connect to the server
    logging.info("Trying to connect to the server...")
    self.state = GameState.CONNECTING
    status = self.network.connect()
    time.sleep(.1)
        
    if not status:
      # Put the program in error state
      self.leds.on(Colors.RED)
      self.state = GameState.ERROR
    else:
      self.state = GameState.WAITING
      logging.info("Connected!")

def main():
  logging.basicConfig(level=logging.DEBUG)

  game = GameManager()
  
  while True:
    button = game.buttons.await_event()
    logging.info("button event: {}".format(button))
    
    if game.state is GameState.INPUT_COLORCODE:
      buffer = []
      buffer.append(button)
      while game.active_game is None:
        # Wait for next color code input
        button = game.buttons.await_event()
        buffer.append(button)

        print("Current buffer: {}".format(buffer)) 

        # Buffer is too short yet
        if len(buffer) < 8:
          print("Buffer too short")
          continue
        elif len(buffer) == 8:
          # Check if buffer matches
          print("Check color code")
          for game in game.game_list:
            code = game['colorCode']
            print("Color match found: " + game['colorCode'])
            if code == buffer:
              game.active_game = game
              break
          # Pop first item of buffer
          print("Remove first buffer item")
          buffer.pop(0)
    elif game.state is GameState.INPUT_REGULAR:
      pass

    elif game.state is GameState.ERROR:
      restart_program()

def restart_program():
  game
  os.system("python3 main.py")
  time.sleep(0.2)
  quit()

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

if __name__ == "__main__":
  main()
