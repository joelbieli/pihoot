import ledmanager
import buttonmanager
from sense_hat import SenseHat

from colors import Colors
from time import sleep


ledManager = ledmanager.SenseHatLEDManager()
'''

ledManager.on(Colors.RED)
ledManager.on(Colors.BLUE)
ledManager.on(Colors.GREEN)
ledManager.on(Colors.YELLOW)

ledManager.set_indicator_light((127, 18, 128))
#ledManager.set_indicator_light((0, 0, 0))


sense = SenseHat()
event = sense.stick.wait_for_event()
print("The joystick was {} {}".format(event.action, event.direction))
sleep(0.1)
event = sense.stick.wait_for_event(emptybuffer=True)
print("The joystick was {} {}".format(event.action, event.direction))
'''
buttonManager = buttonmanager.SenseHatButtonManager()

while True:
	ledManager.toggle(buttonManager.await_event())




