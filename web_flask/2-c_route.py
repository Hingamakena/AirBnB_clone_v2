#!/usr/bin/python3

""" from flask import Flask for namespace
    
    initialize app with the flask Namespace """
app = Flask(__name__)

""" display "Hello HBNB" """
@app.route("/")
def main():
    return "Hello HBNB"

""" display "hbnb" in capital letters """
@app.route("/hbnb")
def hbnb():
    return "HBNb"

""" Route C followed by the value of the text variable """
@app.route("/c/<text>")
def c():
    return f"{text}"
