# Circuit Python
My CircuitPython assignment (Elisabeth Scharf)
The files in this repository are all CircuitPython assignments completed so far. These modules were designed to help us learn how to code with the Circuit Python language.

Here is a super helpful link for [formatting your README file.](https://help.github.com/en/articles/basic-writing-and-formatting-syntax)

# Assignments:
- ## LED fade
**Goal:**

Learn how to use the Circuit Python coding language and turn on the built-in LED on the new Metro Express board. 

**Lessons learned:**
1. Again, Google is your friend. The PWM setup in this code is a bit complicated, but I found different codes that did something similar to what I wanted to do and pieced together the commands. 
2. elif loops are cool! They are used just like any other loop, and then are like the else if loops in Arduino. 
3. The print() function is a great way to troubleshoot. If the code doesn't seem to be functioning properly, just add a print() in the part that is having issues. This will show you if the code is even reading to that part. 
<img src="Media/Final%20LED%20fade%20fritzing%20diagram%20image.PNG" width="800">

- ## Servo assignment
**Goal:**

Code for a servo so that it moves in one direction when you touch one wire and moves in the other direction when you touch the other wire. (And doesn't move at all when no wire is touched.)

**Lessons learned:**

1. Use pseudocode to understand the logic of what is supposed to happen first, and then figure out the technical terms. I knew what it was supposed to do, but I didn't know the "vocabulary" needed to write it. 
2. Split up your code into specific actions to make it doable. For example, start with just making the servo move. Then figure out how capacitive touch works. Then see if you can use capacitive touch to make it move. Then figure out the other capacitive touch wire and how to make it go backwards. 

- ## Photointerrupter
**Goal:**

Have the code print how many times the photointerrupter has been interrupted and print that every 4 seconds. 

**Lessons learned:**
1. There is almost always more that one way to do something. We had learned to use time.sleep() to add time to our code, but in this assignment we weren't allow to use it. This required us to do some research and realize that there is a thing called time.monotonic that can do almost the same thing. 
2. Again, variables are your friend. We used nowT  in order to keep track of the time and now and last to count the number of interrupts. 
3. Again, pseudocode is super helpful! It took me a long time to grasp how the every-four-seconds thing worked, but talking through it without any of the fancy coding words helped me to understand it. Ex. If the time NOW is PAST TIME + 4, then four seconds have passed. So I can say that if (The time it is now)-4 = the last time I checked the time, then I can go ahead with the rest of the commands. 

- ## LCD screen
**Goal:**

 Write code that controls an LCD screen to print the number of button presses and to change directions when the switch is flipped. 

**Lessons Learned:**
1. Buttons and switches are super easy and they are set up the same way. 
(Set up a pin, whether it is INPUT or OUTPUT and pull it up or down)
2. Google is your friend! I got a lot of code for the LCD screen from websites that explain how it works. 
3. Variables are very helpful. I created now and last variables in order to make sure that it only counted the button press one time, not counting up the whole time the button was pressed. It is super easy to establish a variable, just do: (variable = _____), and they make the logic part of the code simple. 
<img src="Media/Final%20LCD%20screen%20fritzing%20diagram%20image.PNG" width="800">
- ## RGB and rgb
**Goal:** 

Learn how to use classes and modules in Circuit Python to make a nice clean code. 

**Lesssons learned:**

1. Variables are great! I made variables for the pins just to make the code a little cleaner.
2. Drawing a picture or talking with other people helps you to understand the logic of the code before you get caught up in the actual commands. For the rainbow part we talked through how we could make each section work and used a drawing to explain it. This made what had seemed like a very complicated task actually quite easy. 
3. Use examples and build off of them. I looked up examples of the code that didn't have to do with this specific task and saw how they used the different commands associated with classes and modules and then figured out how to make them apply to my task. 
<img src="Media/Final%20RGB%20fritzing%20diagram%20image.PNG" width="800">
- ## Hello VS code
**Goal:**

Hello_VS_code was a very simple assignment to help us get used to the format of VS code. 

**Lessons learned:**
1. VS code is very handy because you can push to github straight from there and don't need GitBash. 
2. Editing your README from here is so easy! As I'm typing I can see a preview of what it will look like on the github website. 

- ## Fancy LED
**Goal:**

 Continue using classes and modules and figure out how to do cool things with six LEDs. 

**Lessons learned:**

1. Document your work as you go!! This assignment was so similar to RGB/rgb assignment and if I had done a bit of a better job understanding the code and commenting it, it would have been much easier to pick it up again and write the Fancy LED code
2. Split the code into simple parts. My fancyLED code looks really long and complicated, but it's actually super simple. It pretty much just has lots of commands to turn certain LEDs on or off and an occasional delay. The logic was more complicated than the code itself. A helpful command to know: self.(variable).value = True (or False) will turn an LED on or off. 
<img src="Media/Final%20Fancy%20LED%20fritzing%20diagram%20image.PNG" width="800">




