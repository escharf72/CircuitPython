import time
import board
import pulseio
import touchio
from adafruit_motor import servo

#This tells the servo where to start
angle=0

pwm = pulseio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

#These two variable are part of the capacative touch part of the assignment
touch_A4 = touchio.TouchIn(board.A4)
touch_A5 = touchio.TouchIn(board.A5)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

while True:
    #First if statement: If I touch the wire (A4) then make the servo move one way. 
    if touch_A4.value:
        print("Touched A4!")
        if angle < 180:
           angle +=1
           my_servo.angle = angle
           time.sleep(0.05)
    #Second if statement: If I touch the second wire (A5) then make the servo move the other way.
    if touch_A5.value:
        print("Touched A5!")
        if angle < 180:
            #Subtracting from or adding to the angle (angle -= 1 or angle += 1 makes the servo move) 
            angle -= 1
            my_servo.angle = angle
            time.sleep(0.05)
