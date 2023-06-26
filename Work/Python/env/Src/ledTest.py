import RPi.GPIO as GPIO
import time
btn = 17
Gpio_Pin_Num = [20,21,22,23,24,25,26]
Seven_Seg_Num = ((1,1,1,1,1,1,0), #0
                (0,1,1,0,0,0,0), #1
                (1,1,0,1,1,0,1), #2
                (1,1,1,1,0,0,1), #3
                (0,1,1,0,0,1,1), #4
                (1,0,1,1,0,1,1), #5
                (1,0,1,1,1,1,1), #6
                (1,1,1,0,0,0,0), #7
                (1,1,1,1,1,1,1), #8
                (1,1,1,1,0,1,1)) #9
GPIO.setmode(GPIO.BCM)
GPIO.setup(Gpio_Pin_Num[0],GPIO.OUT)
GPIO.setup(Gpio_Pin_Num[1],GPIO.OUT)
GPIO.setup(Gpio_Pin_Num[2],GPIO.OUT)
GPIO.setup(Gpio_Pin_Num[3],GPIO.OUT)
GPIO.setup(Gpio_Pin_Num[4],GPIO.OUT)
GPIO.setup(Gpio_Pin_Num[5],GPIO.OUT)
GPIO.setup(Gpio_Pin_Num[6],GPIO.OUT)
GPIO.setup(btn, GPIO.IN)
i = 0
while True:
  Value = GPIO.input(btn)
  if Value == True:
    #for i in range(10):
    GPIO.output(Gpio_Pin_Num[0],Seven_Seg_Num[i][0])
    GPIO.output(Gpio_Pin_Num[1],Seven_Seg_Num[i][1])
    GPIO.output(Gpio_Pin_Num[2],Seven_Seg_Num[i][2])
    GPIO.output(Gpio_Pin_Num[3],Seven_Seg_Num[i][3])
    GPIO.output(Gpio_Pin_Num[4],Seven_Seg_Num[i][4])
    GPIO.output(Gpio_Pin_Num[5],Seven_Seg_Num[i][5])
    GPIO.output(Gpio_Pin_Num[6],Seven_Seg_Num[i][6])
    if i != 9:
      i = i+1
    else:
     i = 0
    time.sleep(0.3)
GPIO.cleanup()
