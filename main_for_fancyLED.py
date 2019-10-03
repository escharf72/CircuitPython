import board #pylint: disable-msg=import-error
from fancyLED import FancyLED

L1 = board.D2
L2 = board.D3
L3 = board.D4
L4 = board.D5
L5 = board.D6
L6 = board.D7

fancy1 = FancyLED(L1,L2,L3)
fancy2 = FancyLED(L4,L5,L6)

while True:
    fancy1.alternate()
    fancy2.blink()
    fancy1.chase()
    fancy2.sparkle()