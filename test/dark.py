import board
import RPi.GPIO as GPIO
import time

channel = 20
GPIO.setmode(GPIO.BCM)

# Setup your channel
GPIO.setup(channel, GPIO.OUT)
GPIO.output(channel, GPIO.LOW)

while True:
    # To test the value of a pin use the .input method
    channel_is_on = GPIO.input(channel)  # Returns 0 if OFF or 1 if ON
    
    if channel_is_on:
        print("ON!")
        # Do something here
    else:
        print("off")
    time.sleep(1)
