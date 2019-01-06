import RPi.GPIO as gpio
import time

pin = 26

gpio.setmode(gpio.BCM)
gpio.setup(pin,gpio.OUT)


x = 1

while x <= 5:
    gpio.output(pin, gpio.HIGH)
    time.sleep(5)
    gpio.output(pin, gpio.LOW)
    time.sleep(5)
    x += 1

gpio.cleanup()
