# The commented error message below is super helpful because it allows the computer to use the library and ignore the error
import digitalio #pylint: disable-msg=import-error
from digitalio import DigitalInOut, Direction, Pull #pylint: disable-msg=import-error
import time
import board #pylint: disable-msg=import-error
import random #pylint: disable-msg=import-error

print("let's go!")  #Troubleshooting code 

#This is really similar to the rgb code thing. I have a class and am defining actions that the code can perform. 
class FancyLED :
    # Every time it does this init. It makes these output pins so that I can control them and tell the LEDs to turn on and off 
    def __init__(self, p1, p2, p3):
        print("you just made an object!")
        self.L1 = p1
        self.L2 = p2
        self.L3 = p3

        self.L1 = DigitalInOut(p1)
        self.L1.direction = Direction.OUTPUT
        self.L2 = DigitalInOut(p2)
        self.L2.direction = Direction.OUTPUT
        self.L3 = DigitalInOut(p3)
        self.L3.direction = Direction.OUTPUT

        # Alternate means that the middle will turn off while the outer two are on and then the middle will be on and the others off 
        # (True = on and False = off)
    def alternate(self):
        print("alternate now")
        self.L1.value = True 
        self.L2.value = False
        self.L3.value = True
        time.sleep(1)
        self.L1.value = False
        self.L2.value = True
        self.L3.value = False
        time.sleep(0.5)
        self.L2.value = False

# Chase has the LEDs turning on and off going down the line. 
# logic: Turn one on. Then turn on the next one. Then turn off the previous and turn on the next. Then turn off the previous. Etc...
    def chase(self):
        self.L1.value = True
        time.sleep(0.1) 
        self.L2.value = True
        time.sleep(0.1) 
        self.L1.value = False
        time.sleep(0.1)
        self.L3.value = True
        time.sleep(0.1)
        self.L2.value = False
        time.sleep(0.1)
        self.L3.value = False
        time.sleep(1)

# Blink = turn all on and then turn all off (easy!!) 
    def blink(self):
        self.L1.value = True
        self.L2.value = True
        self.L3.value = True
        time.sleep(1)
        self.L1.value = False
        self.L2.value = False
        self.L3.value = False
        time.sleep(1)
    
# For sparkle we used a random function to make it cooler. The function is imported at the top of the code
    def sparkle(self):
        for whatever in range(0,50):  #I want it to randomly flash 50 different times 
            n= random.randint(0,3)   #It randomly chooses a number from 0-3 and then I tell it what to do for each of the numbers
            print (n)
            if n==0:
                self.L1.value = True
                self.L2.value = True
                self.L3.value = True
            if n==1:
                self.L1.value = False
                self.L2.value = False
                self.L3.value = True
            if n==2:
                self.L1.value = True
                self.L2.value = False
                self.L3.value = False
            if n==3:
                self.L1.value = False
                self.L2.value = True
                self.L3.value = False
            time.sleep(.05)
            # If you don't turn them all off at the end of each command it gets really confusing. 
            self.L1.value = False
            self.L2.value = False
            self.L3.value = False

