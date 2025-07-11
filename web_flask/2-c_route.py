#!/usr/bin/python3

""" from flask import Flask for namespace
    
    initialize app with the flask Namespace """
app = Flask(__name__)


@app.route("/")
def main():
    """ route to display Hello HBNB """
    return "Hello HBNB"

@app.route("/hbnb")
def hbnb():
    """ display HBNB at the output """
    return "HBNb"

@app.route("/c/<text>")
def c():
    """ display C followed by the value of the text """
    return f"{text}"
