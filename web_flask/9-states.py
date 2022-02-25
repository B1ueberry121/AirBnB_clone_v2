#!/usr/bin/python3
"""module that starts flask dev server"""
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


@app.route('/cities_by_states', strict_slashes=False)
def city_state_list():
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    ''' returns list of City objects'''
    states = storage.all(State).values()
    state_obj = None
    for obj in states:
        if obj.id == id:
            state_obj = obj
    return render_template('9-states.html', states=states,
                           id=id, state_obj=state_obj)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
