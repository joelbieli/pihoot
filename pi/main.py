import gpiozero
import time
import logging
import enum
import os

from colors import Colors
from buttonmanager import GPIOButtonManager
from ledmanager import GPIOLEDManager
from loader import Loader
from network import NetworkManager

class GameManager(object):
  def __init__(self):
    self.state = GameState.STARTING;
    self.leds = GPIOLEDManager()
    self.buttons = GPIOButtonManager()
    loader = Loader(self.leds)
    self.network = NetworkManager("10.0.0.1", 65853)
    
    # Display the intro
    self.intro()
    
    # Try to connect to the server
    logging.info("Trying to connect to the server...")
    loader.start()
    status = self.network.connect()
    loader.finish()
    time.sleep(.2)
    
    if not status:
      # Put the program in an endless loop
      self.leds.on(Colors.RED)
      self.state = GameState.ERROR
    else:
      self.leds.blink(Colors.GREEN, 2)
      logging.info("Connected!")
    
  def intro(self):
    for i in range(4):
      self.leds.toggle(Colors.BLUE)
      self.leds.toggle(Colors.RED)
      self.leds.toggle(Colors.YELLOW)
      self.leds.toggle(Colors.GREEN)
      time.sleep(.1)
      self.leds.toggle(Colors.BLUE)
      self.leds.toggle(Colors.RED)
      self.leds.toggle(Colors.YELLOW)
      self.leds.toggle(Colors.GREEN)
      time.sleep(.1)

def main():
  logging.basicConfig(level=logging.DEBUG)

  game = GameManager()
  
  while True:
    button = game.buttons.await_event()
    logging.info("button event: {}".format(button))
    
    if game.state is GameState.RUNNING:
      if button is Colors.BLUE:
        pass
      elif button is Colors.RED:
        pass
      elif button is Colors.YELLOW:
        pass
      else:
        pass
    elif game.state is GameState.ERROR:
      restart_program()

def restart_program():
  os.system("python3 main.py")
  time.sleep(0.2)
  quit()

class GameState(enum.Enum):
  STARTING = 1
  CONNECTING = 2
  RUNNING = 3
  ERROR = 4

if __name__ == "__main__":
  main()
