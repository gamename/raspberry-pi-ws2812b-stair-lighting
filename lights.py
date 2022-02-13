import board
import neopixel
import RPi.GPIO as GPIO
import time

MAX_PIXELS = 300
SHINE_TIMER = 45
TOP_OF_STAIRS_PIN = 23
BOTTOM_OF_STAIRS_PIN = 24
AMBIENT_LIGHT_PIN = 21

pixels = neopixel.NeoPixel(board.D18, MAX_PIXELS)

GPIO.setwarnings(False)

# Refer pins by their sequence number on the board
GPIO.setmode(GPIO.BCM)

# Read output from PIR motion sensor
GPIO.setup(TOP_OF_STAIRS_PIN, GPIO.IN)
GPIO.setup(BOTTOM_OF_STAIRS_PIN, GPIO.IN)
GPIO.setup(AMBIENT_LIGHT_PIN, GPIO.OUT)
GPIO.output(AMBIENT_LIGHT_PIN, GPIO.LOW)

while True:
    # room_dark = GPIO.input(AMBIENT_LIGHT_PIN)
    # Accidentally fried the relay. Set this to true on a temp basis
    room_dark = True

    if room_dark:
        if GPIO.input(TOP_OF_STAIRS_PIN):
            # print("Motion detected at the TOP of stairs!!")
            for count in range(0, MAX_PIXELS, 1):
                pixels[count] = (255, 0, 0)
            time.sleep(SHINE_TIMER)
            for count in range(0, MAX_PIXELS, 1):
                pixels[count] = (0, 0, 0)
        elif GPIO.input(BOTTOM_OF_STAIRS_PIN):
            # print("Motion detected at the BOTTOM of stairs!!")
            for count in range(MAX_PIXELS - 1, 0, -1):
                pixels[count] = (0, 0, 255)
            time.sleep(SHINE_TIMER)
            for count in range(MAX_PIXELS - 1, 0, -1):
                pixels[count] = (0, 0, 0)
        else:
            # print("No motion, all okay.")
            pass
    else:
        # print("room NOT dark")
        pass
