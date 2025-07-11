#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "hello flask app"

if __name__ == "__main__":
    app.run()
