#This code is a simplified command code. rgb is the code where I have lots of code and lots of explanations for the 
# different commands that are in this code. 
from rgb import RGB   # import the RGB class from the rgb module
import board
import time

#I established variables for each of the pins to make things easier
r1 = board.D2
g1 = board.D3
b1 = board.D4
r2 = board.D5
g2 = board.D7
b2 = board.D1

myRGB1 = RGB(r1,g1,b1)   # create a new RGB object, using pins 2, 3, and 4 (RGB LED #1)
myRGB2 = RGB(r2,g2,b2)   # create a new RGB object, using pins 5, 6, and 7 (RGB LED #2)

#This a function that I have in my rgb code to establish certain pins to related to a specific group
myRGB1.change_pins(r1,g1,b1)
myRGB2.change_pins(r2,g2,b2)
#These next four lines are totally unhelpful, but they are two functions that I can use in the future
print(myRGB1.kind)
print(myRGB2.kind)
myRGB1.change_name("rex")
print(myRGB1.name)

myRGB1.red()        # Glow red
myRGB2.green()        # Glow green
time.sleep(1)
myRGB1.blue()         # Glow blue
myRGB2.cyan()         # Blue + green
time.sleep(1)
myRGB1.magenta()      # Red + blue
myRGB2.yellow()       # Red + green
time.sleep(1)
# extra spicy (optional) part
myRGB1.rainbow() # Fade through the colors of the rainbow at the given rate.  Oooooh, pretty!
#time.sleep(1)
