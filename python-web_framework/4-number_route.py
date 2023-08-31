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

@app.route('/python/', defaults={'text': "is_cool"})
@app.route("/python/<text>", strict_slashes=False)
def display_py(text):
    return "Python " + text.replace("_", " ")

@app.route("/number/<int:n>", strict_slashes=False)
def display_number(n):
    if isinstance(n, int):
        return f"{n} is a number"
    
if __name__ == "__main__":
    app.run(debug='True', port=5000, host='0.0.0.0')