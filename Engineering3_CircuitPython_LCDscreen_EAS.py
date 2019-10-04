#Import is a action that allows you to include libraries of code and it makes your life a lot easier! 
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
import board
from digitalio import DigitalInOut, Direction, Pull
import time

# Here I'm establishing a button and a switch. (They are created the same way.) 
button = DigitalInOut(board.D8)
button.direction = Direction.INPUT # (Input= giving information, Output = receiving info/commands)
button.pull = Pull.UP 

switch = DigitalInOut(board.D7)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

# Talk to the LCD at I2C address 0x27.
# The number of rows and columns defaults to 4x20, so those arguments could be omitted in this case.
lcd = LCD(I2CPCF8574Interface(0x3f), num_rows=2, num_cols=16)

# Setting where I want the words to print
lcd.set_cursor_pos(1, 4)
lcd.print("Here I am")
time.sleep(0.1)
lcd.clear()

counter = 0

# I used a variable to make sure the counter didn't just run for the whole time I pushed the button down.
# To do this, I created two variables: now and last, to see if the button had just been pressed or if it was being pressed for a while.
now = True
last = True

switchValue = True

while True:
    now = button.value 
    switchValue = switch.value
    print(str(switchValue))
    if now == False and last == True:  # (If it is currently on, but didn't used to be on, now do this:)
        lcd.set_cursor_pos(0,0)
        lcd.print("Pushed")
        lcd.set_cursor_pos(1,1)
        lcd.print(str(counter))
        time.sleep(0.05)
        lcd.print("  ")
        #lcd.clear()
        now = True
        #This part deals with the switch. If it is pushed one way the counter goes up, and if it is pushed the other way, it goes down.
        if switchValue:
            counter += 1
        if not switchValue:
            counter -= 1

    last = button.value #Resetting last
    time.sleep(0.05)
