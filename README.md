# Circuit Python
My CircuitPython assignment (Elisabeth Scharf)
The files in this repository are all CircuitPython assignments completed so far. These modules were designed to help us learn how to code with the Circuit Python language. 

# Assignments:
- ## LED fade
Goal:
Learn how to use the Circuit Python coding language and turn on the built-in LED on the new Metro Express board. 

Lessons learned:
1. Again, Google is your friend. The PWM setup in this code is a bit complicated, but I found different codes that did something similar to what I wanted to do and pieced together the commands. 
2. elif loops are cool! They are used just like any other loop, and then are like the else if loops in Arduino. 
3. The print() function is a great way to troubleshoot. If the code doesn't seem to be functioning properly, just add a print() in the part that is having issues. This will show you if the code is even reading to that part. 

- ## Servo assignment
Goal:
Code for a servo so that it moves in one direction when you touch one wire and moves in the other direction when you touch the other wire. (And doesn't move at all when no wire is touched.)

Lessons learned:

1. Use pseudocode to understand the logic of what is supposed to happen first, and then figure out the technical terms. I knew what it was supposed to do, but I didn't know the "vocabulary" needed to write it. 
2. Split up your code into specific actions to make it doable. For example, start with just making the servo move. Then figure out how capacitive touch works. Then see if you can use capacitive touch to make it move. Then figure out the other capacitive touch wire and how to make it go backwards. 

- ## Photointerrupter
Goal:
Have the code print how many times the photointerrupter has been interrupted and print that every 4 seconds. 

Lessons learned:
1. There is almost always more that one way to do something. We had learned to use time.sleep() to add time to our code, but in this assignment we weren't allow to use it. This required us to do some research and realize that there is a thing called time.monotonic that can do almost the same thing. 
2. Again, variables are your friend. We used nowT  in order to keep track of the time and now and last to count the number of interrupts. 
3. Again, pseudocode is super helpful! It took me a long time to grasp how the every-four-seconds thing worked, but talking through it without any of the fancy coding words helped me to understand it. Ex. If the time NOW is PAST TIME + 4, then four seconds have passed. So I can say that if (The time it is now)-4 = the last time I checked the time, then I can go ahead with the rest of the commands. 
- ## LCD screen
Goal:
- Write code that controls an LCD screen to print the number of button presses and to change directions when the switch is flipped. 

Lessons Learned:   
1. Buttons and switches are super easy and they are set up the same way. 
(Set up a pin, whether it is INPUT or OUTPUT and pull it up or down)
2. Google is your friend! I got a lot of code for the LCD screen from websites that explain how it works. 
3. Variables are very helpful. I created now and last variables in order to make sure that it only counted the button press one time, not counting up the whole time the button was pressed. It is super easy to establish a variable, just do: (variable = _____), and they make the logic part of the code simple. 
<img src="Media/Final%20LCD%20screen%20fritzing%20diagram%20image.PNG" width="1000">
- ## RGB and rgb
- ## Hello VS code
Goal:
Hello_VS_code was a very simple assignment to help us get used to the format of VS code. 

Lessons learned:
1. VS code is very handy because you can push to github straight from there and don't need GitBash. 
2. Editing your README from here is so easy! As I'm typing I can see a preview of what it will look like on the github website. 

- ## Fancy LED




