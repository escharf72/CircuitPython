import time
import board
import pulseio
from digitalio import DigitalInOut, Direction

# PWM (fading) LEDs are connected to D0 
pwm_leds = board.D0
pwm = pulseio.PWMOut(pwm_leds, frequency=1000, duty_cycle=0)

# digital LEDs connected on D2
digital_leds = DigitalInOut(board.D2)
digital_leds.direction = Direction.OUTPUT #It is an output because it receives commands from the code. (turn on/ turn off/ fade)
brightness = 0  # how bright the LED is at the current moment
fade_amount = 1285  # 2% steping of 2^16
counter = 0  # counter to keep track of cycles


while True:

    # And send to LED as PWM level
    pwm.duty_cycle = brightness

    # change the brightness for next time through the loop:
    brightness = brightness + fade_amount
    # As I change the duty cycle (aka brightness) I can make the LED fade)
    print(brightness)
    # Printing is a good troubleshooting technique to make sure that the coding is functioning properly.

    # reverse the direction of the fading at the ends of the fade:
    if brightness <= 0:
        fade_amount = -fade_amount
        counter += 1
        
    elif brightness >= 65535:  #(elif is a cool combo of else() and if() loops) 
        fade_amount = -fade_amount
        counter += 1

    # wait for 15 ms to see the dimming effect
    time.sleep(.015)

    # turns on the other LEDs every four times through the fade 
    if counter % 4 == 0:
        digital_leds.value = True
    else:
        digital_leds.value = False
