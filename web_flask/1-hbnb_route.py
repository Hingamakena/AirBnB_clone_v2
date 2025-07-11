#!/usr/bin/python3
""" from flask module import Flask """
from flask import Flask

""" declare namespaec of app """
app = Flask(__name__)

@app.route("/", strict_slashes=False)
""" route to the  root folder"""

def main():
    """ return a string to the front_end of the app """
    return "Hello HBNB"

if __name__ == "__main__":
    """ run on port 5000 with host listening at 00.0.0 """
    app.run(port=5000, host="0.0.0.0")
