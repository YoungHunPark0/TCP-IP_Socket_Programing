import RPi.GPIO as GPIO
import time

swPin = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(swPin, GPIO.IN)

def my_callback(channel):
	print("Interrupt !!")

GPIO.add_event_detect(swPin, GPIO.RISING, callback=my_callback)

try:
	while True:
		pass
except KeyboardInterrupt:
	GPIO.cleanup()
