import board
import neopixel
import RPi.GPIO as GPIO
import time

MAX_PIXELS = 300
TRANSIT_DELAY = 30
TOP_OF_STAIRS_PIN = 23
BOTTOM_OF_STAIRS_PIN = 24

pixels = neopixel.NeoPixel(board.D18, MAX_PIXELS)

GPIO.setwarnings(False)

# Refer pins by their sequence number on the board
GPIO.setmode(GPIO.BCM)

# Read output from PIR motion sensor
GPIO.setup(TOP_OF_STAIRS_PIN, GPIO.IN)
GPIO.setup(BOTTOM_OF_STAIRS_PIN, GPIO.IN)

while True:
    if GPIO.input(TOP_OF_STAIRS_PIN):
        # print("Motion detected 23!!")
        for count in range(0, MAX_PIXELS, 1):
            pixels[count] = (255, 0, 0)
        time.sleep(TRANSIT_DELAY)
        for count in range(0, MAX_PIXELS, 1):
            pixels[count] = (0, 0, 0)
    elif GPIO.input(BOTTOM_OF_STAIRS_PIN):
        # print("Motion detected 24!!")
        for count in range(MAX_PIXELS - 1, 0, -1):
            pixels[count] = (255, 255, 255)
        time.sleep(TRANSIT_DELAY)
        for count in range(MAX_PIXELS - 1, 0, -1):
            pixels[count] = (0, 0, 0)
    else:
        # print("No motion, all okay.")
        time.sleep(1)
    time.sleep(0.5)
