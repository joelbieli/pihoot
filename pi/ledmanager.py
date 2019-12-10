import gpiozero
import time

from colors import Colors

class LEDManager(object):
  def __init__(self):
    self._led_dict = {
      Colors.BLUE: gpiozero.LED(16),
      Colors.RED: gpiozero.LED(20),
      Colors.YELLOW: gpiozero.LED(23),
      Colors.GREEN: gpiozero.LED(21),
    }
    
  def on(self, color):
    self._led_dict[color].on()
  
  def off(self, color):
    self._led_dict[color].off()
    
  def toggle(self, color):
    self._led_dict[color].toggle()
    
  def blink(self, color, duration=.1):
    self._led_dict[color].on()
    time.sleep(duration)
    self._led_dict[color].off()
