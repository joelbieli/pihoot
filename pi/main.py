import gpiozero

def main():
  logging.basicConfig(level=logging.DEBUG)

  game = GameManager()
  
  while True:
    button = game.buttons.await_event()
    logging.info("button event: {}".format(button))
    
    if game.state is GameState.RUNNING:
      if button is Colors.BLUE:
        pass
      elif button is Colors.RED:
        pass
      elif button is Colors.YELLOW:
        pass
      else:
        pass
    elif game.state is GameState.ERROR:
      restart_program()

if __name__ == "__main__":
  main()
