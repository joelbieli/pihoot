import gpiozero
import time
import queue
import abc

from sense_hat import SenseHat
from colors import Colors

class _ButtonManager(object):
  __metaclass__ = abc.ABCMeta

  @classmethod
  def version(self): return "1.0"
  
  # This method is called by the event loop on the beginning of every loop
  @abc.abstractmethod
  def await_event(self, color): raise NotImplementedError

'''
Button manager implementation for GPIO
'''
class GPIOButtonManager(_ButtonManager):
  def __init__(self, is_listening=True):
    self._event_queue = queue.Queue()
    self.is_listening = is_listening
    
    self._button_blue = gpiozero.Button(27)
    self._button_blue.when_released = lambda: self._put_event(Colors.BLUE)

    self._button_red = gpiozero.Button(23)
    self._button_red.when_released = lambda: self._put_event(Colors.RED)

    self._button_yellow = gpiozero.Button(25)
    self._button_yellow.when_released = lambda: self._put_event(Colors.GREEN)

    self._button_green = gpiozero.Button(5)
    self._button_green.when_released = lambda: self._put_event(Colors.YELLOW)

  def _put_event(self, color):
    if self.is_listening:
      self._event_queue.put(color)

  def await_event(self):
    return self._event_queue.get(True, None)

'''
Button manager implementation for SenseHat
'''
class SenseHatButtonManager(_ButtonManager):
  def __init__(self, is_listening=True):
    self.is_listening = is_listening
    self.sense = SenseHat()
    
    self._button_dict = {
      "right": Colors.BLUE,
      "down": Colors.GREEN,
      "left": Colors.YELLOW,
      "up": Colors.RED
    }

  def await_event(self):
    if self.is_listening:
      while True:
        event = self.sense.stick.wait_for_event(emptybuffer=True)
        if event.action == "pressed" and event.direction != "middle":
          return self._button_dict[event.direction]
      
