from microbit import *
from OC11 import OC11

OC11 = OC11()

OC11.init()

while True:
      for i in range(1, 3):
        OC11.writePin(i, True)
        sleep(3000)
        
      for i in range(2, 0, -1):
        OC11.writePin(i, False)
        sleep(3000)
