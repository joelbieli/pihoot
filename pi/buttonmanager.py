import gpiozero
import time
import queue

from colors import Colors

class ButtonManager(object):
  def __init__(self, is_listening=True):
    self._event_queue = queue.Queue()
    self.is_listening = is_listening
    
    self._button_blue = gpiozero.Button(27)
    self._button_blue.when_released = lambda: self._put_event(Colors.BLUE)

    self._button_red = gpiozero.Button(24)
    self._button_red.when_released = lambda: self._put_event(Colors.RED)

    self._button_yellow = gpiozero.Button(12)
    self._button_yellow.when_released = lambda: self._put_event(Colors.GREEN)

    self._button_green = gpiozero.Button(22)
    self._button_green.when_released = lambda: self._put_event(Colors.YELLOW)

  def _put_event(self, color):
    if self.is_listening:
      self._event_queue.put(color)

  def await_event(self):
    print("Await...")
    return self._event_queue.get(True, None)
