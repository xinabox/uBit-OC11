from microbit import *
from OC11 import OC11

OC11 = OC11.OC11()

OC11.init()

while True:
    for i in range(0, 2):
        OC11.write(i, True)
        sleep(500)
        
    for i in range(2, 0, -1):
        OC11.write(i, False)
        sleep(500)