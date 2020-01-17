import zmq
import logging
import threading
import enum

class NetworkManager(object):
  def __init__(self, address, port, game_manager):
    self.address = address
    self.port = port
    self.conn = None
    self._game_manager = game_manager

    self._context = zmq.Context()
    
  def connect(self):
    self._socket = self._context.socket(zmq.SUB)
    self._socket.connect("tcp://10.0.0.10:5563")
    self._socket.setsockopt(zmq.SUBSCRIBE, _Topic.QUEUE_GAMES.value)
    self._socket.setsockopt(zmq.SUBSCRIBE, _Topic.START_QUESTION.value)
    self._socket.setsockopt(zmq.SUBSCRIBE, _Topic.END_QUESTION.value)

    self._listener = threading.Thread(self.socket_routine)
    self._listener.start()

  def socket_routine(self):
    while True:
      topic = self._socket.recv_string()

      if topic is _Topic.QUEUE_GAMES.value:
        data = self._socket.recv_json()

        # Update games list and set to listening
        self._game_manager.games_list = data
        

  def games_update(games):
    self.game_manager.games = games


class _Topic(enum.Enum):
  QUEUE_GAMES = "queueingGames"
  START_QUESTION = "startQuestion"
  END_QUESTION = "endQuestion"