from flask import Flask, render_template, request

import RPi.GPIO as GPIO
import time

app = Flask(__name__)

servo = 22
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo, GPIO.OUT)
p = GPIO.PWM(servo, 50)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/feedfish")
def feed():
    print("feed function fired")
    feed_fish()
    return 200, OK

def feed_fish():

    print("feed_fish fired")

    try:

        print("in the try loop")
        p.start(12)
        p.ChangeDutyCycle(12)
        time.sleep(1)
        p.ChangeDutyCycle(7.5)
        time.sleep(1)
        #p.ChangeDutyCycle(5)
        #time.sleep(1)
        #p.ChangeDutyCycle(2.5)
        #time.sleep(1)
        p.ChangeDutyCycle(0)

    except: 
        GPIO.cleanup()

if __name__  == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)

