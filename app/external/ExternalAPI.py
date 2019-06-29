from flask import (jsonify, request)
from flask_restful import Resource, reqparse
from .services import get_external_book_info
from app.helpers.services import non_empty_string

class ExternalAPI(Resource):

    def get(self):

        self.parser = reqparse.RequestParser()
        self.parser.add_argument("name", type=non_empty_string, required=True, help='Name cannot be Empty',
                                 location='args')
        print('Parsing')
        args = self.parser.parse_args()
        name = args["name"]
        response = get_external_book_info(name)
        return jsonify(response)