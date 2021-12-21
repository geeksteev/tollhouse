from flask import Flask, render_template
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('subfolder/index.html', status=True)

@app.route('/lightsOn', methods=['POST', 'GET'])
def lightsOn():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)

    red = 11
    green = 13

    while 1 == 1:
        GPIO.output(red, True)
        time.sleep(1)
        GPIO.output(red, False)

        GPIO.output(green, True)
        time.sleep(1)
        GPIO.output(green, False)

    GPIO.cleanup()

@app.route('/lightsOff', methods=['POST', 'GET'])
def lightsOff():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)

    GPIO.cleanup()

    return render_template('subfolder/index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
