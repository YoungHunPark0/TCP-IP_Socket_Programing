import RPi.GPIO as GPIO
import time

swPin = 6
ledPin = 13
buzzPin = 19
flag = False
melody = [500, 1000]
GPIO.setmode(GPIO.BCM)
GPIO.setup(swPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(buzzPin, GPIO.OUT)

buzz = GPIO.PWM(buzzPin, 440)

def callbackfunc(channel):
  global flag
  flag = not flag
  print("Interruppt")

GPIO.add_event_detect(swPin, GPIO.RISING, callback=callbackfunc)

try:
  while True:
    while flag:
      buzz.start(50)
      GPIO.output(ledPin, True)
      buzz.ChangeFrequency(melody[0])
      time.sleep(0.5)
      GPIO.output(ledPin, False)
      buzz.ChangeFrequency(melody[1])
      time.sleep(0.5)
    GPIO.output(ledPin, False)
    buzz.stop()

except KeyboardInterrupt:
  GPIO.cleanup()
