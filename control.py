import pygame
import pygame_gui
#import RPi.GPIO as GPIO
import os
import sys
from subprocess import Popen

#literally just set every thing up {
pygame.init()

pygame.display.set_caption('Quick Start')
screen = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))

manager = pygame_gui.UIManager((800, 600))

button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                             text='Input',
                                             manager=manager)

text = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((5, 10), (790, 35)),
                                            html_text='Insert Coordinates',
                                            manager=manager)

clock = pygame.time.Clock()
input_coordinates = True
theme = ("/Users/s1034274/Desktop/SASA.Comms.Urgent.mp4")
inputArray = []
running = True

# } end set up

# psuedo code

# set up variables
# Easy reset loop
# Check for input
#     if not "WhiteButton" or "fixedPanel":
#          compare input array to codes
#
#
#     else:
#         add to inputArray
# 
# 
# 
# 
# 
# 
# 
# 
# 

while running:
    inputArray = []


while True:
    #Read states of inputs
    #input_state1 = GPIO.input(17)
    #input_state2 = GPIO.input(18)
    #quite_video = GPIO.input(24)

    #If GPIO(17) is shorted to ground
    #if input_state1 != last_state1:
    if (input()==1):
        omxc = Popen(['omxplayer', '-b', theme])
    else:
    #If omxplayer is running and GPIO(17) and GPIO(18) are NOT shorted to ground
        os.system('killall omxplayer.bin')


while input_coordinates:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            input_coordinates = False

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == button:
                    input_coordinates = False

        manager.process_events(event)

    manager.update(time_delta)

    screen.blit(background, (0, 0))
    manager.draw_ui(screen)

    pygame.display.update()

text = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((5, 10), (790, 35)),
                                            html_text='Input Launch Code',
                                            manager=manager)

input_code = True

while input_code:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            input_code = False

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == button:
                    input_code = False

        manager.process_events(event)

    manager.update(time_delta)

    screen.blit(background, (0, 0))
    manager.draw_ui(screen)

    pygame.display.update()

text = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((5, 10), (790, 35)),
                                            html_text='Ready To Launch',
                                            manager=manager)

launch = True

while launch:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launch = False

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == button:
                    launch = False

        manager.process_events(event)

    manager.update(time_delta)

    screen.blit(background, (0, 0))
    manager.draw_ui(screen)

    pygame.display.update()

text = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((5, 10), (790, 35)),
                                            html_text='Launching...',
                                            manager=manager)

launching = True

while launching:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launching = False

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == button:
                    launching = False

        manager.process_events(event)

    manager.update(time_delta)

    screen.blit(background, (0, 0))
    manager.draw_ui(screen)

    pygame.display.update()