# // control led strip - group 1
#
# void setup() {
#   Serial.begin(9600);
#   pinMode(2, OUTPUT);
#   digitalWrite(2,HIGH);
# }
#
# void loop() {
#   while (Serial.available() > 0) {     //wait for data available
#     String teststr = Serial.readString();  //read until timeout
#     Serial.print(teststr);
#     teststr.trim();
#     if (teststr == "on") {
#       digitalWrite(2, LOW);
#     } else if (teststr == "off") {
#       digitalWrite(2, HIGH);
#     }
#   }
# }
#
#

# python

import serial
import time
import requests

ser = serial.Serial('COM43',9600)
current_content = b'0'

if ser.is_open:
    ser.close()
ser.open()


while True:
    v = requests.get('http://192.168.100.138:5000/grupa1rec')
    print(v.content)
    if v.content != current_content:
        current_content=v.content
        if v.content == b'1':
            ser.write(b'on');
        else:
            ser.write(b'off');

ser.close()