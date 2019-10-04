import board
from digitalio import DigitalInOut, Direction, Pull
import time

# a photointerrupter is set up exactly like a button. (Interuppted = pushed) 
button = DigitalInOut(board.D6)
button.direction = Direction.INPUT
button.pull = Pull.UP

# I created two variables: now and last, to figure out if the button had just been pushed or if it was being held down. 
now = True
last = True
theLastTimeIDidThis = 0 #I created this variable to help with the every-four-seconds component of this code
counter = 0

while True:
    nowT = time.monotonic()
    now = button.value

    # this is the logic to do the thing every 4 seconds
    if nowT - 4 >= theLastTimeIDidThis:  # In other words, if four seconds have passed... 
        print("I have been interrupted:")
        print (str(counter))
        time.sleep(0.05)
        theLastTimeIDidThis = time.monotonic()  #Reset the counter

    # this is the logic to see if the photointerrupter just got interrupted
    if now == False and last ==  True:
        counter += 1
        #print(counter)
    time.sleep(0.05)
    last = now

