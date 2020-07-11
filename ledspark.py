#!/usr/bin/python3

import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import urllib.request as urllib

sensor = Adafruit_DHT.DHT11

pin = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        str = '溫度:{:.1f}, 濕度:{:.0f}%'.format(temperature, humidity)
        print(str)

        with open('dht.html', 'w') as f:
            f.write(' <html><head><meta charset="utf-8"<meta http-equiv="refresh"content="5"></head><body><h1>')
            f.write('<script>')
            f.write('parent.document.getElementById("dht").innerHTML = "' + str + '";')
            f.write('</script>')
            f.write('</h1></body></html>')
            f.flush()
   # response = urllib.urlopen('https://api.thingspeak.com/update?api_key=G2J9RGIKJG8ZA1H0&field1={}&field2={}'.format(humidity, temperature))

        time.sleep(5)

      
