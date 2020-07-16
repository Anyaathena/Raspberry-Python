import RPi.GPIO as GPIO
import time

pinBN= 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinBN, GPIO.IN)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

buttondown = 0

try:
    while True:
        if not GPIO.input(pinBN):
            buttondown += 1
            print (buttondown)
            time.sleep(0.2)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
