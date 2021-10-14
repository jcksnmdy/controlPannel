from typing import Sequence, Text
import pygame
import pygame_gui
#import RPi.GPIO as GPIO
import os
import sys
from subprocess import Popen
from mfrc522 import SimpleMFRC522


#literally just set every thing up {

reader = SimpleMFRC522()


pygame.init()

pygame.display.set_caption('Quick Start')
screen = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))

manager = pygame_gui.UIManager((800, 600))

text = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((5, 10), (790, 35)),
                                            html_text='Out Of Order :( Fix Me',
                                            manager=manager)

clock = pygame.time.Clock()
input_coordinates = True
theme = ("/Users/s1034274/Desktop/SASA.Comms.Urgent.mp4")

inputArray = []
correctSequence = ['R', 'G', 'B', 'Y']
notLaunched = True
fixed = False
correctInput = False
coordinates = False

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 11 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 12 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 13 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 14 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 15 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 16 to be an input pin and set initial value to be pulled low (off)


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

def addInput(button):
    global inputArray, fixed, coordinates, correctInput, text, notLaunched
    if (button == "f"):
        fixed = True
    if (button != "w") and fixed:
        inputArray.insert(button)
    if (button == "w") and fixed:
        try:
            id, text = reader.read()
            coordinates = True
            print(id)
            print(text)
        except:
            print("error")
            GPIO.cleanup()
        if (inputArray == correctSequence):
            inputArray = []
            correctInput = True
        else:
            inputArray = []
    if (button == "l") and correctInput and coordinates and fixed:
        # play vid
        os.system("echo 'playing vid'")
        notLaunched = False

    print(inputArray)

GPIO.add_event_detect(10,GPIO.RISING,callback=addInput("f"),) # Setup event on pin 10 rising edge
GPIO.add_event_detect(11,GPIO.RISING,callback=addInput("w"),) # Setup event on pin 10 rising edge
GPIO.add_event_detect(12,GPIO.RISING,callback=addInput("r"),) # Setup event on pin 10 rising edge
GPIO.add_event_detect(13,GPIO.RISING,callback=addInput("y"),) # Setup event on pin 10 rising edge
GPIO.add_event_detect(14,GPIO.RISING,callback=addInput("g"),) # Setup event on pin 10 rising edge
GPIO.add_event_detect(15,GPIO.RISING,callback=addInput("b"),) # Setup event on pin 10 rising edge
GPIO.add_event_detect(16,GPIO.RISING,callback=addInput("l"),) # Setup event on pin 10 rising edge

while notLaunched:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            notLaunched = False

        manager.process_events(event)

    manager.update(time_delta)

    screen.blit(background, (0, 0))
    manager.draw_ui(screen)

    pygame.display.update()

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