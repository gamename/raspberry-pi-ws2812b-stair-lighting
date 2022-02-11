import board
import neopixel
import RPi.GPIO as GPIO
import time

MAX_PIXELS = 7 
TRANSIT_DELAY = 30
STAIRS_PIN = 21

pixels = neopixel.NeoPixel(board.D18, MAX_PIXELS)

GPIO.setwarnings(False)

# Refer pins by their sequence number on the board
GPIO.setmode(GPIO.BCM)

# Read output from PIR motion sensor
GPIO.setup(STAIRS_PIN, GPIO.IN)

while True:
    if GPIO.input(STAIRS_PIN):
        pixels.fill((255, 255, 255))
        time.sleep(TRANSIT_DELAY)
        pixels.fill((0, 0, 0))
    else:
        time.sleep(1)
    time.sleep(0.5)
