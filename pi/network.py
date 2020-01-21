import zmq
import logging
import threading
import enum
import requests

from gamestate import GameState
from colors import RGBColors

'''
The network manager is responsible for all Network related tasks
It manages the REST client and the socket endpoints
'''
class NetworkManager(object):
  def __init__(self, address, port, game_manager):
    self.address = address
    self.port = port
    self.conn = None
    self._game_manager = game_manager

    self._context = zmq.Context()
  
  '''
  Connect to the server with a address and a port
  '''
  def connect(self):
    self._socket = self._context.socket(zmq.SUB)
    self._socket.connect("tcp://{}:{}".format(self.address, self.port))
    
    # Subscribe to all topics
    self._socket.setsockopt_string(
      zmq.SUBSCRIBE, _Topic.QUEUE_GAMES.value)
    self._socket.setsockopt_string(
      zmq.SUBSCRIBE, _Topic.BEGIN_QUESTION.value)
    self._socket.setsockopt_string(
      zmq.SUBSCRIBE, _Topic.END_QUESTION.value)

    # Start the network socket thread
    self._listener = threading.Thread(target = self.socket_routine)
    self._listener.start()
    
    return True

  '''
  This event loop manages the incoming events from the sockets
  '''
  def socket_routine(self):
    while True:
      topic = self._socket.recv_string()
            
      if topic == _Topic.QUEUE_GAMES.value:
        # Get the data package
        data = self._socket.recv_json()
                
        # Only update games when WAITING_GAMES or INPUT_COLORCODE
        if self._game_manager.state is GameState.WAITING_GAMES or \
           self._game_manager.state is GameState.INPUT_COLORCODE:
          # Update games list and set to listening
          self._game_manager.games_list = data
          self._game_manager.state = GameState.INPUT_COLORCODE
        
      elif _Topic.BEGIN_QUESTION.value in topic:
        data = self._socket.recv_json()
        self._game_manager.active_answer = data
                
        # Wait for begin_question
        self._game_manager.state = GameState.INPUT_REGULAR

      elif _Topic.END_QUESTION.value in topic:           
        self._game_manager.state = GameState.WAITING_QUESTION
  
  '''
  Send a join_game request to the server
  '''
  def join_game(self):
    logging.info("Attempt to join server game_id: {}".format(
      self._game_manager.active_game["id"]))
      
    r = requests.post(
      "http://{}:8080/api/game/{}/join".format(
        self.address,
        self._game_manager.active_game["id"]))
    self._game_manager.leds.set_rgb(RGBColors[r.json()["color"]])
    self._game_manager.active_player = r.json()

  '''
  Send a send_answer request to the server
  '''
  def send_answer(self, color):
    logging.info("Answer to server answer: {} game_id: {}".format(
      color, self._game_manager.active_game["id"]))
      
    requests.post(
      "http://{}:8080/api/game/{}/answer/{}".format(
        self.address,
        self._game_manager.active_game["id"],
        self._game_manager.active_player["id"]),
      data = color.name, headers = {'Content-Type':'text/plain'})
      
  def fetch_games(self):
    logging.info("Fetching games from server")
    
    r = requests.get(
      "http://{}:8080/api/game/queueing".format(self.address)).json()
    if r != []:
      self._game_manager.games_list = r
      self._game_manager.state = GameState.INPUT_COLORCODE

'''
Topics that are used to comunicate with the socket server
'''
class _Topic(enum.Enum):
  QUEUE_GAMES = "queueingGames"
  BEGIN_QUESTION = "beginQuestion"
  END_QUESTION = "endQuestion"
