#!/usr/bin/python3
"""Script for Http Response (CORS)"""

from api.v1.views import app_views
from flask import jsonify


# the status of the api route
@app_views.route('/status', methods=['GET'])
def get_status():
    """Get status of the API"""
    return jsonify({"status": "OK"})
