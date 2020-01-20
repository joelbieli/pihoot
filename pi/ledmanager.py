import gpiozero
import time
import abc

from sense_hat import SenseHat
from colors import Colors
from colors import RGBColors
from colors import RGB_COLORS

'''
Abstract class that defines the interface between LED access and
different hardware.
'''
class _LEDManager(object):
  __metaclass__ = abc.ABCMeta

  @classmethod
  def version(self): return "1.0"
  @abc.abstractmethod
  def set_rgb(self, color): raise NotImplementedError
  @abc.abstractmethod
  def on(self, color): raise NotImplementedError
  @abc.abstractmethod
  def off(self, color): raise NotImplementedError
  @abc.abstractmethod
  def toggle(self, color): raise NotImplementedError
  @abc.abstractmethod
  def blink(self, color, duration=.1): raise NotImplementedError

'''
LED manager implementation for GPIO
'''
class GPIOLEDManager(_LEDManager):
  def __init__(self):
    self._led_dict = {
      Colors.BLUE: gpiozero.LED(22),
      Colors.RED: gpiozero.LED(24),
      Colors.GREEN: gpiozero.LED(12),
      Colors.YELLOW: gpiozero.LED(26),
    }
    self._rgb_led = {
      Colors.RED: gpiozero.LED(16),
      Colors.GREEN: gpiozero.LED(20),
      Colors.BLUE: gpiozero.LED(21)
    }
    
    # Trun off all LEDs
    self.off(Colors.RED)
    self.off(Colors.GREEN)
    self.off(Colors.BLUE)
    self.off(Colors.YELLOW)
    
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

'''
LED manager implementation for SenseHat
'''
class SenseHatLEDManager(_LEDManager):
  def __init__(self):
    r_cords = ((1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (2, 1), (3, 1), (4, 1), (5, 1), (3, 2), (4, 2))
    y_cords = ((0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4))
    g_cords = ((1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (2, 6), (3, 6), (4, 6), (5, 6), (3, 5), (4, 5))
    b_cords = ((7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (6, 2), (6, 3), (6, 4), (6, 5), (5, 3), (5, 4))
    self.i_cords = ( (3, 3), (4, 4), (4, 3), (3, 4))
    
    self._led_dict = {
      Colors.RED: r_cords,
      Colors.GREEN: g_cords,
      Colors.BLUE: b_cords,
      Colors.YELLOW: y_cords
    }
    
    self._color_dict = {
      Colors.RED: (255, 0, 0),
      Colors.GREEN: (0, 255, 0),
      Colors.BLUE: (0, 0, 255),
      Colors.YELLOW: (255, 255, 0)
    }
    
    self.sense = SenseHat()
    
  def on(self, color):
    self._set_led(color)
  
  def off(self, color):
    self._set_led(color, off=True)
    
  def toggle(self, color):
    if self.sense.get_pixel(self._led_dict[color][0][0], self._led_dict[color][0][1]) == [0, 0, 0]:
      self._set_led(color)
    else:
      self._set_led(color, off=True)
    
  def blink(self, color, duration=.1):
    self._set_led(color)
    time.sleep(duration)
    self._set_led(color, off=True)
  
  def set_indicator_light(self, rgb):
    for i in self.i_cords:
      self.sense.set_pixel(i[0], i[1], rgb)
    
  def _set_led (self, color, off=False):
    for i in self._led_dict[color]:
      if not off:
        self.sense.set_pixel(i[0], i[1], self._color_dict[color])
      else:
        self.sense.set_pixel(i[0], i[1], (0, 0, 0))
