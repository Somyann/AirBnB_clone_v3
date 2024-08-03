#!/usr/bin/python3
import app_views from api.v1.views
from flask import jsonify

@app_views.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "OK"})
