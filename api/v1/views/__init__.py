#!/usr/bin/python3
"""Initializing Api Endpoint"""
from flask import Blueprint

# the endpoint
app_views = Blueprint(
    'app_views', __name__, url_prefix='/api/v1'
)

from api.v1.views.index import *
