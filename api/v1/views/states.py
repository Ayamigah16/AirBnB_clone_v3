#!/usr/bin/python3
"""
A new view for State objects that handles all
default RESTFul API actions
"""

from flask import jsonify, request, abort
from api.v1.views import app_views
from models import storage, State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_states():
    """Retrieves the list of all State objects"""
    states = [
        state.to_dict() for state in storage.all(State).values()
    ]
    return jsonify(states)


@app_views.route(
    '/states/<state_id>',
    methods=['GET'],
    strict_slashes=False
)
def get_state(state_id):
    """Retrieves a State object"""
    state = storage.get(State, state_id)
    if state:
        return jsonify(state.to_dict())
    else:
        abort(404)


@app_views.route(
    '/states',
    methods=['POST'],
    strict_slashes=False
)
def create_state():
    """Creates a State"""
    if not request.json:
        abort(400, description="Not a JSON")
    if 'name' not in request.json:
        abort(400, description="Missing name")
    data = request.get_json()
    state = State(**data)
    state.save()
    return jsonify(state.to_dict()), 201


@app_views.route(
    '/states/<state_id>',
    methods=['PUT'],
    strict_slashes=False
)
def update_state(state_id):
    """Updates a State object"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    if not request.json:
        abort(400, description="Not a JSON")
    data = request.get_json()
    for key, value in data.items():
        if key != 'id' and key != 'created_at' and key != 'updated_at':
            setattr(state, key, value)
    state.save()
    return jsonify(state.to_dict())
