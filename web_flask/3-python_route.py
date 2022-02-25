#!/usr/bin/python3
"""module that starts flask dev server"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is(text):
    if text:
        text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def python_is(text=None):
    if text:
        text = text.replace("_", " ")
        return "Python {}".format(text)
    else:
        print("here!")
        return "Python is cool"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
