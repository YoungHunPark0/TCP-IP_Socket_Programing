from flask import Flask, request, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)

@app.route("/")
def home():
	return render_template("index.html")
@app.route("/led/on")
def led_on():
	try:
		GPIO.output(7, GPIO.HIGH)
		return "ok"
	except expression as identifier:
		return "fail"

@app.route("/led/off")
def led_off():
	try:
		GPIO.output(7, GPIO.LOW)
		return "ok"
	except expression as identifier:
		return "fall"
		
if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = '8080', debug = True)
