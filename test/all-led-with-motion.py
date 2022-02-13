import board
import neopixel
import RPi.GPIO as GPIO
import time

MAX_PIXELS = 7 
EGRESS_INTERVAL = 30
STAIRS_PIN = 21
WHITE = (255,255,255)
OFF = (0,0,0)

pixels = neopixel.NeoPixel(board.D18, MAX_PIXELS)

GPIO.setwarnings(False)

# Refer pins by their sequence number on the board
GPIO.setmode(GPIO.BCM)

# Read output from PIR motion sensor
GPIO.setup(STAIRS_PIN, GPIO.IN)

while True:
    try: 
        if GPIO.input(STAIRS_PIN):
            pixels.fill(WHITE)
            time.sleep(EGRESS_INTERVAL)
            pixels.fill(OFF)
    except KeyboardInterrupt:
        pixels.fill(OFF)
        exit()
