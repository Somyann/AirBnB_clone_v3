#!/usr/bin/python3
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views

app = Flask(__name__)

@app.route('/api/v1/stats', methods=['GET'])
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

if __name__ == '__main__':
    app.run(debug=True)
