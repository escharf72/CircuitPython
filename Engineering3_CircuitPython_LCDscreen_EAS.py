from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
import board
from digitalio import DigitalInOut, Direction, Pull
import time


button = DigitalInOut(board.D8)
button.direction = Direction.INPUT
button.pull = Pull.UP

switch = DigitalInOut(board.D7)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

# Talk to the LCD at I2C address 0x27.
# The number of rows and columns defaults to 4x20, so those
# arguments could be omitted in this case.
lcd = LCD(I2CPCF8574Interface(0x3f), num_rows=2, num_cols=16)

#lcd.clear()

# Start at the second line, fifth column (numbering from zero).
lcd.set_cursor_pos(1, 4)
lcd.print("Here I am")
time.sleep(0.1)
lcd.clear()

counter = 0

now = True
last = True
switchValue = True
while True:
    now = button.value
    switchValue = switch.value
    print(str(switchValue))
    if now == False and last == True:
        lcd.set_cursor_pos(0,0)
        lcd.print("Pushed")
        lcd.set_cursor_pos(1,1)
        lcd.print(str(counter))
        time.sleep(0.05)
        lcd.print("  ")
        #lcd.clear()
        now = True
        if switchValue:
            counter += 1
        if not switchValue:
            counter -= 1

    last = button.value
    time.sleep(0.05)