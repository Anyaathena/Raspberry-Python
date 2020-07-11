#!/usr/bin/python3
import RPi.GPIO as GPIO
import cgi
import time

form = cgi.FieldStorage()
text = form.getvalue("times")

print("Content-type:text/html\n")

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

for i in range(int(text)):
    GPIO.output(21,1)
    time.sleep(0.5)
    GPIO.output(21,0)
    time.sleep(1)
