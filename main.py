from flask import Flask, render_template, request
from flask_cors import CORS

app = Flask(__name__, static_folder="static")
CORS(app, resources={r"/api/*": {"origins": "*"}})

part = 2


@app.route('/')
def hello_world():
    return render_template('test_1.html')


relay = False


@app.route('/grupa1')
def gr1():
    if request.method == "GET":
        return render_template('group_1_relay.html', part=part)


@app.route('/grupa1on')
def gr1on():
    global relay
    relay = True
    return 'true'


@app.route('/grupa1off')
def gr1off():
    global relay
    relay = False
    return 'false'


@app.route('/grupa1rec')
def gr1receive():
    if relay:
        return "1"
    else:
        return "0"


bme = ";;"


@app.route('/grupa2', methods=['GET', 'POST'])
def gr2():
    global bme
    if request.method == "GET":
        return render_template('group_2_bme.html', temp=bme.split(';')[0], pres=bme.split(';')[1],
                               humd=bme.split(';')[2], part=part)
    elif request.method == "POST":
        bme = request.args.get("v")
        return "1"


@app.route('/grupa3')
def gr3():
    if request.method == "GET":
        return render_template('group_3_startreq.html', part=part)


@app.route('/grupa4')
def gr4():
    if request.method == "GET":
        return render_template('group_4_rfid.html', part=part)


@app.route('/grupa5')
def gr5():
    if request.method == "GET":
        return render_template('group_5_feed.html', part=part)


@app.route('/grupa6')
def gr6():
    if request.method == "GET":
        return render_template('group_6_control_panel.html', part=part)


@app.route('/grupa7')
def gr7():
    if request.method == "GET":
        return render_template('group_7_co_sensor.html', part=part)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
