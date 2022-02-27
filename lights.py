"""
THis is a script to light a WS2812b LED strip on a flight of stairs using a
raspberry pi!!

There are 3 sensors utilized:
  1. A light sensor at the top of the stairs to determine if it is light or dark (no need to light stairs in daytime).
  2. A motion sensor at the top of the stairs (to detect someone going down)
  3. A motion sensor at the bottom of the stairs (to detect someone going up)

"""
import board
import neopixel
import RPi.GPIO as GPIO
import time

# How many pixels are in the WS2812b strip?k
MAX_PIXELS = 300

# How long should we shine the pixels?
SHINE_TIMER = 120

# How bright should the LEDs be?
BRIGHTNESS = 0.05

# What GPIO pin is associated with a condition?
TOP_OF_STAIRS_INPUT_PIN = 20
BOTTOM_OF_STAIRS_INPUT_PIN = 24
DARK_INDICATOR_PIN = 21

# Use the board internal definition for this
LED_STRIP_OUTPUT_PIN = board.D18

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
OFF = (0, 0, 0)


def top_to_bottom(number_of_pixels, color):
    """
    Light the stairs starting from the top
    :param number_of_pixels: Number of pixels on the ws2812b strip.
    :param color: The color we are setting the strip to.
    """
    for count in range(0, number_of_pixels, 1):
        pixels[count] = color


def bottom_to_top(number_of_pixels, color):
    """
    Light the stairs starting from the bottom
    :param number_of_pixels: Number of pixels on the ws2812b strip.
    :param color: The color we are setting the strip to.
    """
    for count in range(number_of_pixels - 1, 0, -1):
        pixels[count] = color


pixels = neopixel.NeoPixel(LED_STRIP_OUTPUT_PIN, MAX_PIXELS, brightness=BRIGHTNESS)

GPIO.setwarnings(False)

# Refer pins by their sequence number on the board
GPIO.setmode(GPIO.BCM)

# Read output from PIR motion sensor
GPIO.setup(TOP_OF_STAIRS_INPUT_PIN, GPIO.IN)
GPIO.setup(BOTTOM_OF_STAIRS_INPUT_PIN, GPIO.IN)

# Configure the light sensor
GPIO.setup(DARK_INDICATOR_PIN, GPIO.IN)

while True:
    try:
        # IF it is nighttime, switch on the DARK indicator
        if GPIO.input(DARK_INDICATOR_PIN):
            # print("Room DARK")
            if GPIO.input(TOP_OF_STAIRS_INPUT_PIN):
                # print("Motion detected at the TOP of stairs!!")
                top_to_bottom(MAX_PIXELS, WHITE)
                time.sleep(SHINE_TIMER)
                top_to_bottom(MAX_PIXELS, OFF)
            elif GPIO.input(BOTTOM_OF_STAIRS_INPUT_PIN):
                # print("Motion detected at the BOTTOM of stairs!!")
                bottom_to_top(MAX_PIXELS, WHITE)
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
