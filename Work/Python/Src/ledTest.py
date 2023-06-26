import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN)

GPIO.setup(4, GPIO.OUT)  # G
GPIO.setup(11, GPIO.OUT) # F
GPIO.setup(17, GPIO.OUT) # A
GPIO.setup(27, GPIO.OUT) # B
GPIO.setup(9, GPIO.OUT) # E
GPIO.setup(10, GPIO.OUT) # D
GPIO.setup(22, GPIO.OUT) # C

count = 0

OnPin = [[22,27,14,15,18,10],
         [27,14],
         [22,27,9,18,15],
         [22,27,9,14,15],
         [10,9,27,14],
         [22,10,9,14,15],
         [22,10,9,14,15,18],
         [22,27,14],
         [9,10,22,27,18,15,14],
         [22,10,27,9,14]]

while True:
   GPIO.output(9, False)
   GPIO.output(10, False)
   GPIO.output(22, False)
   GPIO.output(27, False)
   GPIO.output(18, False)
   GPIO.output(15, False)
   GPIO.output(14, False)

   value = GPIO.input(24)
   if value == True:
     count = count+1
     print(count)

   if count == 10:
     count = 0
   for i in range(len(OnPin[count])):
     GPIO.output(OnPin[count][i], True)
   time.sleep(0.1)
