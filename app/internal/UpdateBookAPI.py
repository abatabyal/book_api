import json
from flask_restful import Resource, reqparse
from flask import (request, jsonify, abort)
from app.helpers.services import non_empty_string, non_empty_integer, non_empty_list, check_date_format
from datetime import datetime
from app.models.books import Books
from app import db
from sqlalchemy import extract

class UpdateBookAPI(Resource):

    def patch(self, id):
        print("Updating Book: " + str(id))
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("name", type=non_empty_string, help='Name cannot be Empty', location='form')
        self.parser.add_argument('isbn', type=non_empty_string, help='ISBN cannot be Empty', location='form')
        self.parser.add_argument('authors', type=non_empty_list, help='Authors cannot be Empty', action='append', location='form')
        self.parser.add_argument('country', type=non_empty_string, help='Country cannot be Empty', location='form')
        self.parser.add_argument('number_of_pages', type=non_empty_integer, help='Number of pages cannot be Empty',
                                 location='form')
        self.parser.add_argument('publisher', type=non_empty_string, help='Publisher cannot be Empty',
                                 location='form')
        self.parser.add_argument('release_date', type=check_date_format, location='form')
        print('Parsing')
        args = self.parser.parse_args()
        name = args["name"]
        isbn = args["isbn"]
        authors = args["authors"]
        country = args["country"]
        number_of_pages = args["number_of_pages"]
        publisher = args["publisher"]
        release_date = args["release_date"]
        update_book = Books.query.filter_by(id=id).first()

        if name:
            update_book.name = name
            update_book.updated_at = datetime.now()
        if isbn:
            update_book.isbn = isbn
            update_book.updated_at = datetime.now()
        if authors:
            update_book.authors = authors
            update_book.updated_at = datetime.now()
        if country:
            update_book.country = country
            update_book.updated_at = datetime.now()
        if number_of_pages:
            update_book.number_of_pages = number_of_pages
            update_book.updated_at = datetime.now()
        if publisher:
            update_book.publisher = publisher
            update_book.updated_at = datetime.now()
        if release_date:
            update_book.release_date = release_date
            update_book.updated_at = datetime.now()

        if name or isbn or authors or country or number_of_pages or publisher or release_date:
            try:
                db.session.commit()
            except:
                db.session.rollback()
                db.session.remove()
                return jsonify({"message": "Something went wrong while updating. Please try again."})

            response_dict = {}
            data_dict = {}
            data_dict["id"] = update_book.id
            data_dict["name"] = update_book.name
            data_dict["isbn"] = update_book.isbn
            try:
                data_dict['authors'] = json.loads(update_book.authors)
            except:
                data_dict['authors'] = update_book.authors
            data_dict["number_of_pages"] = update_book.number_of_pages
            data_dict["publiser"] = update_book.publisher
            data_dict["country"] = update_book.country
            data_dict["release_date"] = (update_book.release_date).strftime("%Y-%m-%d")
            response_dict["data"] = data_dict
            response_dict["status_code"] = 200
            response_dict["status"] = "success"
            response_dict["message"] = "The book " + update_book.name + " was updated successfully"

            return jsonify(response_dict)
        else:
            abort(400)

    def delete(self, id):
        print("Deleting Book: " + str(id))
        delete_book = Books.query.filter_by(id=id).first()
        name = ''
        if delete_book:
            name = delete_book.name
            try:
                db.session.delete(delete_book)
                db.session.commit()
                response_dict = {}
                data_list = []
                response_dict["data"] = data_list
                response_dict["status_code"] = 200
                response_dict["status"] = "success"
                response_dict["message"] = "The book " + name + " was deleted successfully"
                return jsonify(response_dict)
            except:
                db.session.rollback()
                db.session.remove()
                return jsonify({"message": "Something went wrong while updating. Please try again."})
        else:
            return jsonify({"message": "Book with id: " + str(id) + " does not exist"})

    def get(self, id):
        print("Fetching Book: " + str(id))
        get_book = Books.query.filter_by(id=id).first()
        if get_book:
            response_dict = {}
            data_dict = {}
            data_dict["id"] = get_book.id
            data_dict["name"] = get_book.name
            data_dict["isbn"] = get_book.isbn
            try:
                data_dict['authors'] = json.loads(get_book.authors)
            except:
                data_dict['authors'] = get_book.authors
            data_dict["number_of_pages"] = get_book.number_of_pages
            data_dict["publiser"] = get_book.publisher
            data_dict["country"] = get_book.country
            data_dict["release_date"] = (get_book.release_date).strftime("%Y-%m-%d")
            response_dict["data"] = data_dict
            response_dict["status_code"] = 200
            response_dict["status"] = "success"
            return jsonify(response_dict)
        else:
            abort(404)