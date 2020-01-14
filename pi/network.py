import stomp
import logging

class NetworkManager(object):
  def __init__(self, address, port, game_manager):
    self.address = address
    self.port = port
    self.conn = None
    self._game_manager = game_manager
    
  def connect(self):
    self.conn = stomp.Connection(
    [(self.address, self.port)], timeout=2, reconnect_attempts_max=2)
    self.conn.set_listener('', PiHootListener(self))
    self.conn.start()
    
    try:
      self.conn.connect(wait=True)
    except stomp.exception.ConnectFailedException as ex:
      return False
    return True
    
  def disconnect(self):
    self.conn.disconnect()


class PiHootListener(stomp.ConnectionListener):
    def __init__(self, network_manager):
        super(PiHootListener, self).__init__()
        self._network_manager = network_manager
    
    def on_error(self, headers, message):
        print('received an error "%s"' % message)
    def on_message(self, headers, message):
        print('received a message "%s"' % message)
