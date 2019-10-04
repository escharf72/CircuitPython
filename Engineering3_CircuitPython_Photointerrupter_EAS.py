import board
from digitalio import DigitalInOut, Direction, Pull
import time

button = DigitalInOut(board.D6)
button.direction = Direction.INPUT
button.pull = Pull.UP
now = True
last = True
theLastTimeIDidThis = 0
counter = 0

while True:
    nowT = time.monotonic()
    now = button.value

    # this is the logic to do the thing every 4 seconds
    if nowT - 4 >= theLastTimeIDidThis:
        print("I have been interrupted:")
        print (str(counter))
        time.sleep(0.05)
        theLastTimeIDidThis = time.monotonic()

    # this is the logic to see if the photointerrupter just got interrupted
    if now == False and last ==  True:
        counter += 1
        #print(counter)
    time.sleep(0.05)
    last = now

#monotonic