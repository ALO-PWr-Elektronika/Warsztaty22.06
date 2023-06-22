from flask import Flask, render_template
import serial
import time

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

ser = serial.Serial('COM12',9600)

if ser.is_open:
    ser.close()

ser.open()

@app.route("/data")
def data():
    global b

    b = ser.readline()
    return render_template("data.html",b=b)

