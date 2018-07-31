import time
from waitress import serve
from flask import Flask, render_template, jsonify, request


APP = Flask(__name__)
devices = {}


@APP.route("/")
def index():
    return render_template('index.html')


@APP.route("/get_data", methods=['GET'])
def get_data():
    return jsonify(devices)


@APP.route("/push_data", methods=['POST'])
def push_data():
    data = dict(request.form)
    id_ = data.pop('id', None)[0] # why is this a list idek
    if id_ is not None and id_ not in devices:
        devices[id_] = {}
    for key, value in data.items():
        if key not in devices[id_]:
            devices[id_][key] = []
        devices[id_][key].append((time.time(), float(value[0])))
    return jsonify('Success!')


if __name__ == "__main__":
    serve(APP, port=80)
