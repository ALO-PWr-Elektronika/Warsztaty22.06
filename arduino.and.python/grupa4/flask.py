import threading
import time
import serial
import jinja2

import flask

ser = serial.Serial("COM31", 9600)

if ser.is_open:
    ser.close()


correct = ["A7 1B F7 73"]
his = []

app = flask.Flask(__name__)

@app.route('/')
def main():
    return flask.render_template("index.html", x = his[2:])





def read():
    a = 0
    ser.open()
    
    time.sleep(2)
    while 1==1:
        #i = str(input())
        #ser.write(bytes(i, 'utf-8'))
        line = ser.readline().decode("utf-8")
        line = line.strip()
        print(f"|{line}|")
        
        if line in correct and a == 0:
            #webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
            
            a+=1
        elif not line in correct:
            a = 0
        if line in correct and len(line)<15:
            his.append(f"{line}, success")
            ser.write(b"s")
            
        elif not line in correct:
            his.append(f"{line}, failure")
            ser.write(b"f")
            
    ser.close() 

thread = threading.Thread(target = app.run)
thread2 = threading.Thread(target = read)
thread.start()
thread2.start()
thread.join()
thread2.join()