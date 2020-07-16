import RPi.GPIO as GPIO
import time

pinBN= 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

n = 0
def bnClick(channel):       
    global n
    GPIO.remove_event_detect(channel)
    print(n)
    n += 1
    time.sleep(0.1)
    GPIO.add_event_detect(4, GPIO.FALLING, callback=bnClick, bouncetime=300)
        
try:
    GPIO.add_event_detect(4, GPIO.FALLING, callback = bnClick, bouncetime=300)   
    while True:
        time.sleep(100000)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
