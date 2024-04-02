#!/usr/bin/python3
"""
new view for the link between Place objects
and Amenity objects that handles all default RESTFul API actions
"""

from flask import jsonify, abort
from api.v1.views import app_views
from models import storage


@app_views.route(
    '/places/<place_id>/amenities', methods=['GET'])
def get_place_amenities(place_id):
    place = storage.get("Place", place_id)
    if not place:
        abort(404)

    amenities = [
        amenity.to_dict() for amenity in place.amenities]
    return jsonify(amenities)


@app_views.route(
    '/places/<place_id>/amenities/<amenity_id>',
    methods=['DELETE'])
def delete_place_amenity(place_id, amenity_id):
    place = storage.get("Place", place_id)
    amenity = storage.get("Amenity", amenity_id)

    if not place or not amenity:
        abort(404)
    if amenity not in place.amenities:
        abort(404)

    place.amenities.remove(amenity)
    storage.save()
    return jsonify({}), 200


@app_views.route(
    '/places/<place_id>/amenities/<amenity_id>',
    methods=['POST'])
def link_amenity_to_place(place_id, amenity_id):
    place = storage.get("Place", place_id)
    amenity = storage.get("Amenity", amenity_id)

    if not place or not amenity:
        abort(404)
    if amenity in place.amenities:
        return jsonify(amenity.to_dict()), 200

    place.amenities.append(amenity)
    storage.save()
    return jsonify(amenity.to_dict()), 201
