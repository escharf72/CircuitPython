#This is complicated code behind the simple RGB code. It establishes what all the functions mean. 
import pulseio
import time

# a class is the bigger group in which I can create smaller groups. 
class RGB:
    kind="colors"
    #The init runs every time
    def __init__(self, r, g, b):
        print("you just made an object!") #This is a good way to troubleshoot to make sure that the code is working
        #Here I am establishing the pins (the parts of the tricolor LED) and making them pins that can fade, not just do on/off. 
        self.pwm_r = pulseio.PWMOut(r, frequency=1000, duty_cycle=0)
        self.pwm_g = pulseio.PWMOut(g, frequency=1000, duty_cycle=0)
        self.pwm_b = pulseio.PWMOut(b, frequency=1000, duty_cycle=0)
#Useless part of the code to demonstrate something that you can code for
    def change_name(self, newName):
        self.name = newName
# This is the function that appears at the beginning of the RBG code and it tells the computer to assign certain pins to an LED 
#based on which version of RGB it is. 
    def change_pins(self, r, g, b):
        self.r = r

#All of the following are establishing actions that the code can do:
    # Helpful info: 0 = grounded or "on"     2**16-1 = off 
    #These first two are really simple: just turn on that specific LED color
    def red(self):
        print("this should be red")
        self.pwm_r.duty_cycle= 0
        self.pwm_g.duty_cycle= 2**16-1
        self.pwm_b.duty_cycle = 2**16-1
    def blue(self):
        # do green stuff
        print("this should be blue")
        self.pwm_r.duty_cycle= 2**16-1
        self.pwm_g.duty_cycle= 2**16-1
        self.pwm_b.duty_cycle = 0
    def green(self):
        print("this should be green")
        self.pwm_r.duty_cycle= 2**16-1
        self.pwm_g.duty_cycle= 0
        self.pwm_b.duty_cycle = 2**16-1
    #These next ones are a tiny bit more complicated because you have to mix colors. 
    # Magenta = red+blue  Yellow = red+green  Cyan = green+blue 
    def magenta(self):
        print("this should be magenta")
        self.pwm_r.duty_cycle= 0
        self.pwm_g.duty_cycle= 2**16-1
        self.pwm_b.duty_cycle = 0
    def yellow(self):
        print("this should be yellow")
        self.pwm_r.duty_cycle= 0
        self.pwm_g.duty_cycle= 0
        self.pwm_b.duty_cycle = 2**16-1
    def cyan(self):
        print("this should be cyan")
        self.pwm_r.duty_cycle= 2**16-1
        self.pwm_g.duty_cycle= 0
        self.pwm_b.duty_cycle = 0
       
#This part required some thinking and blending of colors
    def rainbow(self):
        self.pwm_r.duty_cycle= 0  #Start the rainbow with just red on
        self.pwm_g.duty_cycle= 2**16-1
        self.pwm_b.duty_cycle = 2**16-1
     
        for val in range(0,2**16-1, 64):  #This is saying that from 0 (on) to 2**16-1 (off) it will go off in increments of 64
            self.pwm_r.duty_cycle= val    # By making r = val, I am telling it to slowly turn off.
            self.pwm_g.duty_cycle= 2**16-1-val  # By making g = 2*16-1-val, I am telling it to go in the opposite direction and turn on
            self.pwm_b.duty_cycle = 2**16-1     # I don't need blue right now, so it is just off (2**16-1) 
            time.sleep(0.01)
        for val in range(0,2**16-1, 64):
            self.pwm_r.duty_cycle= 2**16-1  # Red is off
            self.pwm_g.duty_cycle= val      # Green is turning off 
            self.pwm_b.duty_cycle = 2**16-1-val  #Blue is turning on 
            time.sleep(0.01)
        for val in range(0,2**16-1, 64):
             self.pwm_r.duty_cycle= 2**16-1-val  # Red is turing on 
             self.pwm_g.duty_cycle= 2**16-1   #Green is off 
             self.pwm_b.duty_cycle = val      #Blue is turing off 
             time.sleep(0.01)
