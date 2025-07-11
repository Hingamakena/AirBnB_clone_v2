#!/usr/bin/python3

""" from flask import Flask for namespace """
from flask import Flask

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

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
