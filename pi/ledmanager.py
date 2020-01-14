import gpiozero
import time
import abc

from colors import Colors
from colors import RGBColors
from colors import RGB_COLORS

class _LEDManager(object):
  __metaclass__ = abc.ABCMeta

  @classmethod
  def version(self): return "1.0"
  @abc.abstractmethod
  def on(self, color): raise NotImplementedError
  @abc.abstractmethod
  def off(self, color): raise NotImplementedError
  @abc.abstractmethod
  def toggle(self, color): raise NotImplementedError
  @abc.abstractmethod
  def blink(self, color, duration=.1): raise NotImplementedError

class GPIOLEDManager(_LEDManager):
  def __init__(self):
    self._led_dict = {
      Colors.BLUE: gpiozero.LED(22),
      Colors.RED: gpiozero.LED(24),
      Colors.YELLOW: gpiozero.LED(26),
      Colors.GREEN: gpiozero.LED(12),
    }
    self._rgb_led = {
      Colors.RED: gpiozero.LED(16),
      Colors.GREEN: gpiozero.LED(20),
      Colors.BLUE: gpiozero.LED(21)
    }
    
  def set_rgb(self, color):
    if RGB_COLORS[color][0]:
      self._rgb_led[Colors.RED].on()
    else:
      self._rgb_led[Colors.RED].off()
      
    if RGB_COLORS[color][1]:
      self._rgb_led[Colors.GREEN].on()
    else:
      self._rgb_led[Colors.GREEN].off()
      
    if RGB_COLORS[color][2]:
      self._rgb_led[Colors.BLUE].on()
    else:
      self._rgb_led[Colors.BLUE].off()

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
