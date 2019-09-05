import time
import board
import pulseio
import touchio
from adafruit_motor import servo

angle=0
#touch_pad = board.A4
#touch_pad1 = board.A5
# create a PWMOut object on Pin A2.
pwm = pulseio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)


touch_A4 = touchio.TouchIn(board.A4)
touch_A5 = touchio.TouchIn(board.A5)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

while True:
    if touch_A4.value:
        print("Touched A4!")
        if angle < 180:
           angle +=1
           my_servo.angle = angle
           time.sleep(0.05)

    if touch_A5.value:
        print("Touched A5!")
        if angle < 180:
            angle -= 1
            my_servo.angle = angle
            time.sleep(0.05)
