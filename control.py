#from typing import Sequence, Text
#import pygame
#import pygame_gui
import RPi.GPIO as GPIO
import os
import sys
from subprocess import Popen
import time
from mfrc522 import SimpleMFRC522
from gpiozero import Button

fixButton = Button(17)


#literally just set every thing up {

reader = SimpleMFRC522()


#pygame.init()

#pygame.display.set_caption('Quick Start')
#screen = pygame.display.set_mode((800, 600))

#background = pygame.Surface((800, 600))
#background.fill(pygame.Color('#000000'))

#manager = pygame_gui.UIManager((800, 600))

#text = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((5, 10), (790, 35)),
#                                            html_text='Out Of Order :( Fix Me',
#                                            manager=manager)

#clock = pygame.time.Clock()
input_coordinates = True


inputArray = []
correctSequence = ['r', 'g', 'b', 'y', 'y', 'r']
notLaunched = True
fixed = False
correctInput = False
coordinates = False
# } end set up

# psuedo code

# set up variables
# Easy reset loop
# Check for input
#      if "white" button pressed and fixed pannel and coordinates entered
#          compare input array to codes
#          if inputArray == correct sequence
#              display launch
#              wait for all launch buttons pressed
#                  launch
#
#      if fixed pannel
#           display 'input coordinates'
#           wait till RFID scan
#               display heading to "sumwhere"
# 
#     else:
#         add to inputArray
# 
# 

def goodCode():
    global inputArray, fixed, coordinates, correctInput, text, notLaunched
    i = 0
    while i < len(correctInput):
        if (correctInput[i]!=inputArray[i]):
            return False
    return True

def addInput(button):
    global inputArray, fixed, coordinates, correctInput, text, notLaunched
    print(button)
    print(inputArray)
    if (button == "f"):
        fixed = True
    elif (button != "w") and fixed:
        inputArray.insert((len(inputArray)-1), button)
    elif (button == "w"):
        if (goodCode()):
            inputArray = []
            correctInput = True
        else:
            inputArray = []
    elif (button == "l") and correctInput and coordinates and fixed:
        # play vid
        os.system("echo 'playing vid'")
        notLaunched = False

    print(inputArray)

print("Started")
while notLaunched:
    print("Fix Panel")
    while not fixed:
        time.sleep(0.1)
        if fixButton.is_pressed:
            addInput("f")
    print("Fixed. Gimme coordinates")
    try:
        id, text = reader.read()
        coordinates = True
        print(id)
        print(text)
    except:
        print("error")
        GPIO.cleanup()
    print("Got 'em. Gimme Code")
    while not correctInput:
        time.sleep(0.01)
    print("Got it. Launch it now")
    
print("LAUNCHED")
    

#figuring out how to play video, i can do audio but not video

# while True:
#     #Read states of inputs
#     #input_state1 = GPIO.input(17)
#     #input_state2 = GPIO.input(18)
#     #quite_video = GPIO.input(24)

#     #If GPIO(17) is shorted to ground
#     #if input_state1 != last_state1:
#     if (input()==1):
#         omxc = Popen(['omxplayer', '-b', theme])
#     else:
#     #If omxplayer is running and GPIO(17) and GPIO(18) are NOT shorted to ground
#         os.system('killall omxplayer.bin')

GPIO.cleanup()