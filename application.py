# wsgi.py
from flask import Flask, jsonify

application = Flask(__name__)

@application.route('/')
def home():
    return jsonify({"roll" : 0})


@application.route('/bug')
def bug():
    return jsonify({"bug" : 1/0})
