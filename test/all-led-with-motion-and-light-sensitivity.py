import board
import neopixel
import RPi.GPIO as GPIO
import time

MAX_PIXELS = 7
SHINE_TIMER = 30
AMBIENT_LIGHT_PIN = 20
STAIRS_PIN = 21

pixels = neopixel.NeoPixel(board.D18, MAX_PIXELS)

GPIO.setwarnings(False)

# Refer pins by their sequence number on the board
GPIO.setmode(GPIO.BCM)

# Read output from PIR motion sensor
GPIO.setup(STAIRS_PIN, GPIO.IN)
GPIO.setup(AMBIENT_LIGHT_PIN, GPIO.OUT)
GPIO.output(AMBIENT_LIGHT_PIN, GPIO.LOW)

while True:
    darkness = GPIO.input(AMBIENT_LIGHT_PIN)
    if darkness:
        if GPIO.input(STAIRS_PIN):
            pixels.fill((255, 255, 255))
            time.sleep(SHINE_TIMER)
            pixels.fill((0, 0, 0))
