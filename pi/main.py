import gpiozero
import time
import logging
import enum
import os

import animator

from colors import RGBColors
from buttonmanager import SenseHatButtonManager
from ledmanager import SenseHatLEDManager
from network import NetworkManager
from gamemanager import GameManager
from gamestate import GameState

def main():
  # Setup logging for background process
  logging.basicConfig(level=logging.DEBUG, filename="/var/tmp/pihoot.log")

  game_manager = GameManager()
  game_manager.network.fetch_games()
  
  event_loop(game_manager)

'''
This is the main event loop. It manages all the button presses by the user
'''
def event_loop(game_manager):
  buffer = []
  while True:
    button = game_manager.buttons.await_event()
    
    # Manual restart mechanism that restarts Pi when a certain color code is entered
    buffer.append(button.name)
    if len(buffer) == 8:
      if buffer == ['RED','BLUE','RED','BLUE','RED','BLUE','RED','BLUE']:
        game_manager.restart()
      buffer.pop(0)
    
    logging.info("Button press: {}".format(button))
    
    if game_manager.state is GameState.INPUT_COLORCODE:

      # Build buffer while checking if user entered a color code
      color_buffer = []
      color_buffer.append(button.name)

      while game_manager.active_game is None:
        # Wait for next color code input
        button = game_manager.buttons.await_event()
        color_buffer.append(button.name)

        # Buffer is too short yet
        if len(color_buffer) < 8:
          time.sleep(.2)
          continue
        elif len(color_buffer) == 8:
          # Check if buffer matches
          for game in game_manager.games_list:
            code = game['colorCode']
            if code == color_buffer:
              game_manager.active_game = game
              game_manager.network.join_game()
              
              game_manager.state = GameState.WAITING_QUESTION
              
              break
          # Pop first item of buffer
          color_buffer.pop(0)
    elif game_manager.state is GameState.INPUT_REGULAR:
      game_manager.network.send_answer(button)
      game_manager.state = GameState.WAITING_QUESTION

    elif game_manager.state is GameState.ERROR:
      game_manager.restart()

if __name__ == "__main__":
  main()
