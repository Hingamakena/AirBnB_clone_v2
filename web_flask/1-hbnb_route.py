#!/usr/bin/python3
""" from flask module import Flask """
from flask import Flask

""" declare namespaec of app """
app = Flask(__name__)

@app.route("/", strict_slashes=False)
""" route to the  root folder """
def main():
    return "Hello HBNB"

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
