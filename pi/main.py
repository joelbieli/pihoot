import gpiozero
import time
import logging
import enum
import os

import animator

from colors import RGBColors
from buttonmanager import GPIOButtonManager
from ledmanager import GPIOLEDManager
from network import NetworkManager
from gamemanager import GameManager
from gamestate import GameState

def main():
  # Setup logging for background process
  logging.basicConfig(level=logging.DEBUG, filename="/var/tmp/pihoot.log")

  game_manager = GameManager()
  event_loop(game_manager)

def event_loop(game_manager):
  while True:
    button = game_manager.buttons.await_event()
    logging.getLogger('pihoot').info("Button press: {}".format(button))
    
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
              game_manager.network.join_game()
              
              game_manager.state = GameState.WAITING_QUESTION
              
              break
          # Pop first item of buffer
          buffer.pop(0)
    elif game_manager.state is GameState.INPUT_REGULAR:
      game_manager.network.send_answer(button)
      game_manager.state = GameState.WAITING_QUESTION

    elif game_manager.state is GameState.ERROR:
      game_manager.restart()

if __name__ == "__main__":
  main()
