#!/usr/bin/python3
"""
create Flask app; app_views
"""

from flask import  jsonify
from models import storage
from api.v1.views import app_views


@app_views.route('/status')
def api_status():
    """
    Return a JSON response for RESTful API health.
    """
    response = {'status': "OK"} # type: ignore
    return jsonify(response)



@app.route@app_views.route('/api/v1/stats', methods=["GET"], strict_slashes=False)
def get_stats():
    """
    Endpoint that retrieves the number of each object by type.
    """
    stats = {
        'Amenity': storage.count('Amenity'),
        'City': storage.count('City'),
        'Place': storage.count('Place'), 
        'Review': storage.count('Review'),
        'State': storage.count('State'),
        'User': storage.count('User')
    }
    return jsonify(stats)


