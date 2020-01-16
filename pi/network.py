import zmq
import logging

class NetworkManager(object):
  def __init__(self, address, port, game_manager):
    self.address = address
    self.port = port
    self.conn = None
    self._game_manager = game_manager
    
  def connect(self):
    self.conn = stomp.Connection12(
    [(self.address, self.port)], timeout=3, reconnect_attempts_max=2)
    self.conn.set_listener('pi_listener', PiListener())
    
    try:
      self.conn.start()
      self.conn.connect(wait=True)
            
      self.conn.subscribe('/ws/pi/games', 123)
    except (ConnectionRefusedError, stomp.exception.ConnectFailedException) as ex:
      return False
    return True
    
  def games_update(games):
    self.game_manager.games = games
    
  def disconnect(self):
    self.conn.disconnect()


class PiListener(stomp.ConnectionListener):
    #def __init__(self, network_manager):
    #    super(PiHootListener, self).__init__()
    #    self._network_manager = network_manager
    
    def on_error(self, headers, message):
        print('on_error {} {}'.format(message, headers))
    def on_send(self, headers):
        print("on_send {}".format(headers))
    def on_message(self, headers, message):
        print('on_message {} {}'.format(message, headers))
        
    def on_connected(self, headers):
        print('on_connected {}'.format(headers))
