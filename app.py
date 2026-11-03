from flask import flask

app = Flask(__name__)

def add(a, b):
    return a + b
