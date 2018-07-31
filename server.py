import time
from waitress import serve
from collections import defaultdict
from flask import Flask, render_template, jsonify, request


APP = Flask(__name__)
data = defaultdict(list)


@APP.route("/")
def index():
    return render_template('index.html')


@APP.route("/get_data", methods=['GET'])
def get_data():
    return jsonify(data)


@APP.route("/push_data", methods=['POST'])
def push_data():
    for key, value in request.form.items():
        data[key].append((time.time(), float(value)))
    return jsonify('Success!')


if __name__ == "__main__":
    serve(APP, port=80)
