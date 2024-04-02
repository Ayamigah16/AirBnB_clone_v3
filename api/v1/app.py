#!/usr/bin/python3
"""Rest Api driver"""

from flask import Flask
from api.v1.views import app_views
import os
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """Closes storage session"""
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    """Handle 404 errors"""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', '5000'))
    app.register_blueprint(app_views)
    app.run(host=host, port=port, threaded=True)
