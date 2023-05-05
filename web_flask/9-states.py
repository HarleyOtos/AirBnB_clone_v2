#!/usr/bin/python3
"""
Starts a Flask web application
"""
from flask import Flask
from flask import render_template
from models import storage, State, City


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Closes the database session after each request"""
    storage.close()


@app.route('/states')
def display_states():
    """Displays all states and their cities"""
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>')
def display_state(id):
    """Displays a state and its cities"""
    state = storage.get(State, id)
    if state is None:
        return render_template('9-states.html', not_found=True)
    else:
        cities = sorted(state.cities, key=lambda x: x.name)
        return render_template('9-states.html', state=state, cities=cities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
