import zmq
import logging
import threading
import enum
import requests

from gamestate import GameState
from colors import RGBColors

class NetworkManager(object):
  def __init__(self, address, port, game_manager):
    self.address = address
    self.port = port
    self.conn = None
    self._game_manager = game_manager

    self._context = zmq.Context()
    
  def connect(self):
    self._socket = self._context.socket(zmq.SUB)
    self._socket.connect("tcp://{}:{}".format(self.address, self.port))
    self._socket.setsockopt_string(zmq.SUBSCRIBE, _Topic.QUEUE_GAMES.value)
    self._socket.setsockopt_string(zmq.SUBSCRIBE, _Topic.START_QUESTION.value)
    self._socket.setsockopt_string(zmq.SUBSCRIBE, _Topic.END_QUESTION.value)

    self._listener = threading.Thread(target = self.socket_routine)
    self._listener.start()
    
    return True

  def socket_routine(self):
    while True:
      topic = self._socket.recv_string()
      
      if topic == _Topic.QUEUE_GAMES.value:
        data = self._socket.recv_json()

        # Update games list and set to listening
        self._game_manager.games_list = data
        self._game_manager.state = GameState.INPUT_COLORCODE
        
        logging.debug("Games: {}".format(data))
      elif topic == _Topic.START_QUESTION.value:
        data = self._socket.recv_json()
        
        
        
  def join_game(self):
    r = requests.post(
      "http://{}:8080/api/game/{}/join".format(
        self.address, self._game_manager.active_game["id"]))
    print(r.json())
    self._game_manager.leds.set_rgb(RGBColors[r.json()["color"]])
    self._game_manager.active_player = r.json()

  def send_answer(self, color):
    requests.post(
      "http://{}:8080/api/game/{}/join".format(
        self.address, self._game_manager.active_game["id"],
        data = {"AnswerColor": color}))

class _Topic(enum.Enum):
  QUEUE_GAMES = "queueingGames"
  START_QUESTION = "startQuestion"
  END_QUESTION = "endQuestion"
