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
    return "C " + text.replace("_", " ")

@app.route('/python/', defaults={'text': "is_magic"})
@app.route("/python/<text>", strict_slashes=False)
def display_py(text):
    return "Python " + text.replace("_", " ")

if __name__ == "__main__":
    app.run(debug='True', port=5000, host='0.0.0.0')