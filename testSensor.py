import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.IN)

i = 0
while (i < 5):
    time.sleep(1)
    print(GPIO.input(23))
    i = i+1