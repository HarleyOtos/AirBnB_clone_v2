#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import environ

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.teardown_appcontext
def teardown_db(exception):
    """Removes the current SQLAlchemy Session"""
    storage.close()

@app.route('/hbnb', methods=['GET'])
def hbnb():
    """Displays a HTML page like 8-index.html"""
    states = sorted(storage.all(State).values(), key=lambda s: s.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda a: a.name)
    places = sorted(storage.all(Place).values(), key=lambda p: p.name)
    return render_template('100-hbnb.html', states=states,
                           amenities=amenities, places=places)

if __name__ == '__main__':
    host = '0.0.0.0'
    port = 5000
    if 'HBNB_API_HOST' in environ:
        host = environ['HBNB_API_HOST']
    if 'HBNB_API_PORT' in environ:
        port = int(environ['HBNB_API_PORT'])
    app.run(host=host, port=port)
