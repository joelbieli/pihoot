import threading

from colors import Colors

class Loader(threading.Thread):
  def __init__(self, leds):
    self.leds = leds
    self._is_done = False
    
    super(Loader, self).__init__()
   
  def run(self):
    while not self._is_done:
      self.leds.blink(Colors.BLUE)
      self.leds.blink(Colors.RED)
      self.leds.blink(Colors.GREEN)
      self.leds.blink(Colors.YELLOW)
  
  def finish(self):
    self._is_done = True
