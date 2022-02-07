import board
import neopixel
import RPi.GPIO as GPIO
import time

MAX_PIXELS = 300

pixels = neopixel.NeoPixel(board.D18, MAX_PIXELS)

GPIO.setwarnings(False)

#Refer pins by their sequence number on the board
GPIO.setmode(GPIO.BCM)

#Read output from PIR motion sensor
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)

while True:
    if GPIO.input(23):
#        print("Motion detected 23!!")
        for count in range(0,MAX_PIXELS,1):
            pixels[count] = (0, 0, 255)
        time.sleep(5)
        for count in range(0,MAX_PIXELS,1):
            pixels[count] = (0, 0, 0)
    elif GPIO.input(24):
#        print("Motion detected 24!!")
        for count in range(MAX_PIXELS-1,0,-1):
            pixels[count] = (0, 255, 255)
        time.sleep(5)
        for count in range(MAX_PIXELS-1,0,-1):
            pixels[count] = (0, 0, 0)
    else:
#        print("No motion, all okay.")
        time.sleep(1)
    time.sleep(0.5)
