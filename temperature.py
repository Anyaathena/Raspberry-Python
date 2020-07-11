#!/usr/bin/python3

import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import urllib.request as urllib

sensor = Adafruit_DHT.DHT11

pin = 4
pinLed = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinLed, GPIO.OUT)

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        print('溫度:{:.1f}, 濕度:{:.0f}%'.format(temperature, humidity))

    response = urllib.urlopen('https://api.thingspeak.com/update?api_key=G2J9RGIKJG8ZA1H0&field1={}&field2={}'.format(humidity, temperature))

    time.sleep(5)

    if temperature >= 31:
        GPIO.output(pinLed, 1)
    elif temperature <= 28:
        GPIO.output(pinLed, 0)


      
