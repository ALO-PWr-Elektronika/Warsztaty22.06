

import serial
import time
from flask import Flask, request, render_template

app = Flask(__name__)

ser = serial.Serial("COM5", 9600)

if ser.is_open:
    ser.close()
ser.close()

ser.open()
time.sleep(2)

ser.write(bytes("ping", 'utf-8'))
temp = ser.read()
is_on = False
if temp == "1":
    is_on = True


@app.route('/')
def index():
    if request.method == "GET":
        return render_template('index.html')

@app.route('/on')
def on_led():
    global is_on
    if is_on:
        return "Already on"
    else:
        is_on = True
        ser.write(bytes('on', 'utf-8'))
    return "Successfully turned on"

@app.route('/off')
def off_led():
    global is_on
    if not is_on:
        return "Already off"
    else:
        is_on = False
        ser.write(bytes('off', 'utf-8'))
        return "Successfully turned off"
