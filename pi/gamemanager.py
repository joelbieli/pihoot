import logging
import time
import enum
import os

from buttonmanager import SenseHatButtonManager
from ledmanager import SenseHatLEDManager
from network import NetworkManager

from animator import Animator
from gamestate import GameState

'''
This class managed the whole game. It contains the state, the game and
player id and all the submanagers.
'''
class GameManager(object):
  def __init__(self):
    self.__state = GameState.STARTING
    
    # Game submanagers
    self.leds = SenseHatLEDManager()
    self.buttons = SenseHatButtonManager()
    self.network = NetworkManager("192.168.43.210", 5563, self)
    
    self.games_list = []
    self.active_game = None
    self.active_player = None
    
    # Correct answer color of next question
    self.active_answer = None
    
    self._animator = Animator(self.leds, self)
    self._animator.start()
    time.sleep(1)
    
    # Try to connect to the server
    logging.info("Trying to connect to the server...")
    self.state = GameState.CONNECTING
    status = self.network.connect()
    time.sleep(.5)
        
    if not status:
      # Put the program in error state
      self.state = GameState.ERROR
      logging.error("Failed to connect to the server!")
    else:
      self.state = GameState.WAITING_GAMES
      logging.info("Successfully connected to the server!")

  @property
  def state(self):
    return self.__state

  @state.setter
  def state(self, state):
    self.__state = state
    logging.debug("Gamestate changed to {}".format(state))

  # Restart the whole game
  def restart(self):
    self.state = GameState.RESET
    os.system("python3 /home/pi/Desktop/pihoot/pi/main.py")
    time.sleep(.2)
    print("quit")
    quit()
