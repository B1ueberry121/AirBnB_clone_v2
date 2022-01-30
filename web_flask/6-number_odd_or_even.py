#!/usr/bin/python3
''' Module that Start's a flask dev server '''
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    if text:
        text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def python_text(text=None):
    if text:
        text = text.replace("_", " ")
        return "Python {}".format(text)
    else:
        print("here!")
        return "Python is cool"


@app.route('/number/<int:n>', strict_slashes=False)
def num_n(n):
    if (isinstance(n, int)):
        return "{:d} is a number".format(n)
    else:
        return


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n):
    if (isinstance(n, int)):
        return render_template('5-number.html', number=n)
    else:
        return


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even_template(n):
    if (isinstance(n, int)):
        if n % 2 == 0:
            return render_template('6-number_odd_or_even.html',
                                   number=n, result="even")
            if n % 2 != 0:
                return render_template('6-number_odd_or_even.html', number=n,
                                       result="odd")
            else:
                return


if __name__ == "__main__":
    app.run(host="0.0.0.0")
