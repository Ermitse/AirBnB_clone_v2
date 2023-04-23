#!/usr/bin/python3
""" Starts a Flask web app and fetches data from storage engine """
from flask import Flask, render_template
from models import storage, State, Amenity, Place


app = Flask(__name__)


@app.teardown_appcontext
def close_session(foo):
    """ Closes Session """
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb(id=None):
    """ Displays HTML page """
    states = storage.all(State)
    amenities = storage.all(Amenities)
    places = storage.all(Place)
    return render_template('100-hbnb.html', **locals())


if __name__ == '__main__':
    storage.reload()
    app.run("0.0.0.0", 5000)
