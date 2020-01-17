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
from gamemanager import GameManager
from gamestate import GameState

def main():
  logging.basicConfig(level=logging.DEBUG)

  game_manager = GameManager()
  
  while True:
    button = game_manager.buttons.await_event()
    logging.info("button event: {}".format(button))
    
    if game_manager.state is GameState.INPUT_COLORCODE:
      buffer = []
      buffer.append(button.name)
      while game_manager.active_game is None:
        # Wait for next color code input
        button = game_manager.buttons.await_event()
        buffer.append(button.name)

        # Buffer is too short yet
        if len(buffer) < 8:
          time.sleep(.2)
          continue
        elif len(buffer) == 8:
          # Check if buffer matches
          for game in game_manager.games_list:
            code = game['colorCode']
            if code == buffer:
              game_manager.active_game = game
              game_manager.network.join_game(game["id"])
              
              #self._game_manager.leds.set_rgb(Colors["PURPLE"])
              break
          # Pop first item of buffer
          buffer.pop(0)
    elif game_manager.state is GameState.INPUT_REGULAR:
      pass

    elif game_manager.state is GameState.ERROR:
      game_manager.restart()

if __name__ == "__main__":
  main()
