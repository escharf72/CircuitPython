import board
from digitalio import DigitalInOut, Direction, Pull
import time

button = DigitalInOut(board.D7)
button.direction = Direction.INPUT
button.pull = Pull.UP

while True:
    interrupted = button.value
    if interrupted:
        print("interrupted")
    else:
        print("off")