import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

red = 11
green = 13

while 1 == 1:
    GPIO.output(red, True)
    time.sleep(1)
    GPIO.output(red, False)

    GPIO.output(green, True)
    time.sleep(1)
    GPIO.output(green, False)
GPIO.cleanup()

