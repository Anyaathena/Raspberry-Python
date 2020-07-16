import RPi.GPIO as GPIO
import threading
import time

pinBN= 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def onClick():
    n = 1
    while True:
        channel = GPIO.wait_for_edge(4, GPIO.BOTH, timeout=500000)
        if channel is not None:
            print (n)
            n += 1
            
threading.Thread(target=onClick).start()            
while True:
    time.sleep(100000)


GPIO.cleanup()
