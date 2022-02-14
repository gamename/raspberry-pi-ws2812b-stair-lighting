import board
import RPi.GPIO as GPIO
import time

STAIRS_PIN = 21

GPIO.setwarnings(False)

# Refer pins by their sequence number on the board
GPIO.setmode(GPIO.BCM)

# Read output from PIR motion sensor
GPIO.setup(STAIRS_PIN, GPIO.IN)

while True:
    try: 
        if GPIO.input(STAIRS_PIN):
            print("movement!")
            time.sleep(10)
    except KeyboardInterrupt:
        exit()
