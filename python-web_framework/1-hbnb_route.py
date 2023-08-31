#! /usr/bin/python3

"""
    Your web application must be listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
    You must use the option strict_slashes=False in your route definition
"""

from flask import Flask

app = Flask(__name__)



@app.route("/", strict_slashes=False)
def home():
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    #route for /hbnb
    return "HBNB"

if __name__ == "__main__":
    app.run(debug='True', port=5000, host='0.0.0.0')