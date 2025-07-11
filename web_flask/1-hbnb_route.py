#!/usr/bin/python3
""" from flask module import Flask """
from flask import Flask

""" declare namespaec of app """
app = Flask(__name__)

@app.route("/")
""" route to the  root folder """
def main():
    return "Hello HBNB"
