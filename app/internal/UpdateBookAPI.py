import json
from flask_restful import Resource, reqparse
from flask import (request, jsonify)
from app.helpers.services import non_empty_string, non_empty_integer, non_empty_list, check_date_format
from datetime import datetime
from app.models.books import Books
from app import db
from sqlalchemy import extract

class UpdateBookAPI(Resource):

    def patch(self, id):
        print("Updating Book: " + id)
