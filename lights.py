import board
import neopixel
import RPi.GPIO as GPIO
import time

MAX_PIXELS = 300
SHINE_TIMER = 45
TOP_OF_STAIRS_PIN = 23
BOTTOM_OF_STAIRS_PIN = 24
AMBIENT_LIGHT_PIN = 21

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
OFF = (0, 0, 0)


def top_to_bottom(length, color):
    for count in range(0, length, 1):
        pixels[count] = color


def bottom_to_top(length, color):
    for count in range(length - 1, 0, -1):
        pixels[count] = color


pixels = neopixel.NeoPixel(board.D18, MAX_PIXELS)

GPIO.setwarnings(False)

# Refer pins by their sequence number on the board
GPIO.setmode(GPIO.BCM)

# Read output from PIR motion sensor
GPIO.setup(TOP_OF_STAIRS_PIN, GPIO.IN)
GPIO.setup(BOTTOM_OF_STAIRS_PIN, GPIO.IN)

# Configure the light sensor
GPIO.setup(AMBIENT_LIGHT_PIN, GPIO.OUT)
GPIO.output(AMBIENT_LIGHT_PIN, GPIO.LOW)

while True:
    try:
        # room_dark = GPIO.input(AMBIENT_LIGHT_PIN)
        # Accidentally fried the relay. Set this to true on a temp basis
        room_dark = True
        if room_dark:
            # print("Room DARK")
            if GPIO.input(TOP_OF_STAIRS_PIN):
                # print("Motion detected at the TOP of stairs!!")
                top_to_bottom(MAX_PIXELS, RED)
                time.sleep(SHINE_TIMER)
                top_to_bottom(MAX_PIXELS, OFF)
            elif GPIO.input(BOTTOM_OF_STAIRS_PIN):
                # print("Motion detected at the BOTTOM of stairs!!")
                bottom_to_top(MAX_PIXELS, BLUE)
                time.sleep(SHINE_TIMER)
                bottom_to_top(MAX_PIXELS, OFF)
            else:
                # print("No motion, all okay.")
                pass
        else:
            # print("room NOT dark")
            pass
    except KeyboardInterrupt:
        # print("KeyboardInterrupt pressed")
        pixels.fill(OFF)
        exit()
