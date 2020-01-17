import logging
import time
import enum
import os

from buttonmanager import GPIOButtonManager
from ledmanager import GPIOLEDManager
from network import NetworkManager

from animator import Animator
from gamestate import GameState

class GameManager(object):
  def __init__(self):
    self.__state = GameState.STARTING
    self.leds = GPIOLEDManager()
    self.buttons = GPIOButtonManager()
    self.network = NetworkManager("10.0.0.229", 5563, self)
    self.games_list = []
    self.active_game = None
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
      logging.info("Failed to connect!")
    else:
      self.state = GameState.WAITING_GAMES
      logging.info("Connected!")

  # Debugging
  @property
  def state(self):
    return self.__state

  @state.setter
  def state(self, state):
    self.__state = state
    logging.debug("Gamestate changed to {}".format(state))

  def restart(self):
    self.state = GameState.RESET
    os.system("python3 main.py")
    time.sleep(.2)
    quit()
