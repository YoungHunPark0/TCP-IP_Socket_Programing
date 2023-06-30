import sys
import RPi.GPIO as GPIO
import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5 import QtGui, QtWidgets, uic

ledPin= 7
buzzerPin = 24
melody = [250, 350, 450, 550, 650, 750]
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(buzzerPin, GPIO.OUT)

buzz = GPIO.PWM(buzzerPin, 440)

class qtApp(QWidget):
	def __init__(self):
		super().__init__()
		uic.loadUi('./button.ui', self)
		
		self.Btn_ledon.clicked.connect(self.btnledonClicked)
		self.Btn_ledoff.clicked.connect(self.btnledoffClicked)

	def btnledonClicked(self):
		try:
			GPIO.output(ledPin, GPIO.HIGH)
			
			buzz.start(50)
			for i in range(0, len(melody)):
				buzz.ChangeFrequency(melody[i])
				time.sleep(0.5)
				
		except KeyboardInterrupt:
			GPIO.cleanup()
			
	def btnledoffClicked(self):
		try:
			GPIO.output(ledPin, GPIO.LOW)
			buzz.stop()
				
		except:
			return 'fail'

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = qtApp()
	ex.show()
	sys.exit(app.exec_())
