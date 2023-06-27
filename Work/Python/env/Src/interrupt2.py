import RPi.GPIO as GPIO
import time

swPin = 24
ledPin = 7
flag = False

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(swPin, GPIO.IN)
GPIO.setup(ledPin, GPIO.OUT)

def callbackfunc(channel):
  global flag
  print("Interrupt!!")
  if flag == False:
    flag = True
  elif flag == True:
    flag = False
GPIO.add_event_detect(swPin, GPIO.RISING, callback=callbackfunc)

try:
  while True:
    if flag == True:
      GPIO.output(ledPin, True)
    elif flag == False:
      GPIO.output(ledPin, False)
except KeyboardInterrupt:
  GPIO.cleanup()
