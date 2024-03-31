#!/usr/bin/python3
"""Script for Http Response (CORS)"""

from api.v1.views import app_views
from flask import jsonify
from models import storage


# the status of the api route
@app_views.route('/status', methods=['GET'])
def get_status():
    """Get status of the API"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'])
def get_stats():
    """Gets stats of objects by type"""
    classes = {
        'amenities': 'Amenity',
        'cities': 'City',
        'places': 'Place',
        'reviews': 'Review',
        'states': 'State',
        'users': 'User'
    }
    stats = {key: storage.count(value) for key,value in classes}
    return jsonify(stats)
