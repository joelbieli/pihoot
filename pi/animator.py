import threading
import time

from colors import Colors
from gamestate import GameState

'''
The animator acts as a basic interface between the low level LED manager
and the Game manager. Based on the state of the game, this class
managed the behaviour of the LEDs.
'''
class Animator(threading.Thread):
  def __init__(self, leds, game_manager):
    self._leds = leds
    self._game_manager = game_manager
    self._halting = False

    super(Animator, self).__init__()

  def run(self):
    while True:
      if self._halting:
        time.sleep(1)
      else:
        _ANIM_MAP[self._game_manager.state](self._leds)

  def halt(self, halt=True):
    self._halting = halt

'''
Animation to reset, turn off all LEDs
'''
def _anim_reset(leds):
  leds.off(Colors.RED)
  leds.off(Colors.GREEN)
  leds.off(Colors.BLUE)
  leds.off(Colors.YELLOW)

'''
Wait for color code input, slow blink animation
'''
def _anim_input_colorcode(leds):
  leds.on(Colors.RED)
  leds.on(Colors.GREEN)
  leds.on(Colors.BLUE)
  leds.on(Colors.YELLOW)
  time.sleep(.4)
  leds.off(Colors.RED)
  leds.off(Colors.GREEN)
  leds.off(Colors.BLUE)
  leds.off(Colors.YELLOW)
  time.sleep(.4)

'''
Wait for answer input, turn on all LEDs
'''
def _anim_input_regular(leds):
  leds.on(Colors.RED)
  leds.on(Colors.GREEN)
  leds.on(Colors.BLUE)
  leds.on(Colors.YELLOW)
  time.sleep(.1)

'''
Wait for games, slowly rotate
'''
def _anim_waiting_games(leds):
  leds.on(Colors.BLUE)
  time.sleep(.2)
  leds.off(Colors.BLUE)

  leds.on(Colors.RED)
  time.sleep(.2)
  leds.off(Colors.RED)
  
  leds.on(Colors.GREEN)
  time.sleep(.2)
  leds.off(Colors.GREEN)

  leds.on(Colors.YELLOW)
  time.sleep(.2)
  leds.off(Colors.YELLOW)

'''
Error, turn off all LEDs except for green
'''
def _anim_error(leds):
  leds.off(Colors.BLUE)
  leds.off(Colors.GREEN)
  leds.off(Colors.YELLOW)
  leds.on(Colors.RED)
  time.sleep(.5)

'''
Pi is connecting to server, fast rotating
'''
def _anim_connecting(leds):
  leds.blink(Colors.BLUE)
  leds.blink(Colors.RED)
  leds.blink(Colors.GREEN)
  leds.blink(Colors.YELLOW)

'''
Intro anim, flash all LEDs
'''
def _anim_intro(leds):
  leds.on(Colors.BLUE)
  leds.on(Colors.RED)
  leds.on(Colors.GREEN)
  leds.on(Colors.YELLOW)
  time.sleep(.1)
  leds.off(Colors.BLUE)
  leds.off(Colors.RED)
  leds.off(Colors.GREEN)
  leds.off(Colors.YELLOW)
  time.sleep(.1)

# Most of the Game States are mapped to one specific animation
# some animations are very basic, like just turing everything off
_ANIM_MAP = {
  GameState.STARTING: _anim_intro,
  GameState.CONNECTING: _anim_connecting,
  GameState.ERROR: _anim_error,
  GameState.WAITING_GAMES: _anim_waiting_games,
  GameState.WAITING_QUESTION: _anim_reset,
  GameState.INPUT_REGULAR: _anim_input_regular,
  GameState.INPUT_COLORCODE: _anim_input_colorcode,
  GameState.RESET: _anim_reset
}
