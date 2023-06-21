from flask import Flask, render_template, request
from flask_cors import CORS

relay = False
bme = ";;"

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/')
def hello_world():
    return render_template('test_1.html')


@app.route('/grupa1')
def relay():
    if request.method == "GET":
        return render_template('group_1_relay.html')


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
def receiver():
    if relay:
        return "1"
    else:
        return "0"


@app.route('/grupa2',methods=['GET', 'POST'])
def gr2update():
    global bme
    if request.method == "GET":
        return render_template('group_2_bme.html', temp=bme.split(';')[0], pres=bme.split(';')[1],
                               humd=bme.split(';')[2])
    elif request.method == "POST":
        bme = request.args.get("v")
        return "1"


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
