#!/usr/bin/python3
"""
A new view for User object that handles
all default RESTFul API actions
"""

from flask import jsonify, request, abort
from api.v1.views import app_views
from models import storage, User


@app_views.route(
    '/users', methods=['GET'], strict_slashes=False)
def get_users():
    """Retrieves the list of all User objects"""
    users = storage.all(User).values()
    return jsonify([user.to_dict() for user in users])


@app_views.route(
    '/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """Retrieves a User object"""
    user = storage.get(User, user_id)
    if user:
        return jsonify(user.to_dict())
    else:
        abort(404)


@app_views.route(
    '/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """Deletes a User object"""
    user = storage.get(User, user_id)
    if user:
        storage.delete(user)
        storage.save()
        return jsonify({})
    else:
        abort(404)


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    """Creates a User"""
    if not request.json:
        abort(400, description="Not a JSON")
    if 'email' not in request.json:
        abort(400, description="Missing email")
    if 'password' not in request.json:
        abort(400, description="Missing password")
    data = request.get_json()
    user = User(**data)
    user.save()
    return jsonify(user.to_dict()), 201


@app_views.route(
    '/users/<user_id>',
    methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    """Updates a User object"""
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    if not request.json:
        abort(400, description="Not a JSON")
    data = request.get_json()
    for key, value in data.items():
        if key not in ['id', 'email', 'created_at', 'updated_at']:
            setattr(user, key, value)
    user.save()
    return jsonify(user.to_dict()), 200
