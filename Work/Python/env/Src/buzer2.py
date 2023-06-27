import RPi.GPIO as GPIO
import time
import sys

GPIO.setwarnings(False)
buzzerPin = 17
melody = [261, 293, 329, 349, 391, 440, 493]
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzerPin, GPIO.OUT)

buzz = GPIO.PWM(buzzerPin, 440)

buzz.start(50)

while True:
	try:
		ch = int(input())
		buzz.ChangeFrequency(melody[ch])
		time.sleep(0.3)
		
	except KeyboardInterrupt :
		sys.exit()
	
