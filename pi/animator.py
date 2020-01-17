import threading
import time

from colors import Colors
from main import GameState

_anim_map = {
  GameState.STARTING: _anim_intro,
  GameState.CONNECTING: _anim_connecting,
  GameState.ERROR: _anim_error,
  GameState.WAITING_GAMES: _anim_waiting_games,
  GameState.WAITING_QUESTION: _anim_reset,
  GameState.INPUT_REGULAR: _anim_input_regular,
  GameState.INPUT_COLORCODE: _anim_input_regular,
  GameState.RESET: _anim_reset
}

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
        _anim_map[self._game_manager.state](self._leds)

  def halt(self, halt=True):
    self._halting = halt

def _anim_reset(leds):
  leds.off(Colors.RED)
  leds.off(Colors.GREEN)
  leds.off(Colors.BLUE)
  leds.off(Colors.YELLOW)

def _anim_input_colorcode(leds):
  leds.on(Colors.RED)
  leds.on(Colors.GREEN)
  leds.on(Colors.BLUE)
  leds.on(Colors.YELLOW)
  time.sleep(.3)
  leds.off(Colors.RED)
  leds.off(Colors.GREEN)
  leds.off(Colors.BLUE)
  leds.off(Colors.YELLOW)
  time.sleep(.3)

def _anim_input_regular(leds):
  leds.on(Colors.RED)
  leds.on(Colors.GREEN)
  leds.on(Colors.BLUE)
  leds.on(Colors.YELLOW)
  time.sleep(.1)

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

def _anim_error(leds):
  leds.off(Colors.BLUE)
  leds.off(Colors.GREEN)
  leds.off(Colors.YELLOW)
  leds.on(Colors.RED)
  time.sleep(.5)

def _anim_connecting(leds):
  leds.blink(Colors.BLUE)
  leds.blink(Colors.RED)
  leds.blink(Colors.GREEN)
  leds.blink(Colors.YELLOW)

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
