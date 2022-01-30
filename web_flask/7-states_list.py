#!/usr/bin/python3
''' Module that start's a Flask dev server '''
from flask import Flask, render_template, g
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route('/states_list', strict_slashes=False)
def state_list():
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
