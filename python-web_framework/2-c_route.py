#! /usr/bin/python3

"""
    Basic flask web server
"""

from flask import Flask

app = Flask(__name__)



@app.route("/", strict_slashes=False)
def home():
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def display(text):
    return "c " + text.replace("_", " ")

if __name__ == "__main__":
    app.run(debug='True', port=5000, host='0.0.0.0')