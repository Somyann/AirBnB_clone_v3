#!/usr/bin/python3
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Import everything from the 'api.v1.views.index' module
from api.v1.views.index import *
