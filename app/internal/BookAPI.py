import json
from flask_restful import Resource, reqparse
from flask import (request, jsonify)
from app.helpers.services import non_empty_string, non_empty_integer, non_empty_list, check_date_format
from datetime import datetime
from app.models.books import Books
from app import db
from sqlalchemy import extract

class BookAPI(Resource):

    def post(self):
        """Takes input in form of json
        @name: string
        @isbn: string
        @authors: list of string
        @country: string
        @number of pages: integer
        @publisher: string
        @release date: 'YYYY-MM-DD'
        :return: status code 201 on successful creation of a book record in database
        """
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("name", type=non_empty_string, required=True, help='Name cannot be Empty',
                                 location='json')
        self.parser.add_argument('isbn', type=non_empty_string, required=True, help='ISBN cannot be Empty',
                                 location='json')
        self.parser.add_argument('authors', type=non_empty_list, required=True, help='Authors cannot be Empty',
                                 location='json')
        self.parser.add_argument('country', type=non_empty_string, required=True, help='Country cannot be Empty',
                                 location='json')
        self.parser.add_argument('number_of_pages', type=non_empty_integer, required=True,
                                 help='Number of pages cannot be Empty',
                                 location='json')
        self.parser.add_argument('publisher', type=non_empty_string, required=True, help='Publisher cannot be Empty',
                                 location='json', nullable=False)
        self.parser.add_argument('release_date', type=check_date_format, required=True, location='json')
        print('Parsing')
        request.get_json(force=True)
        args = self.parser.parse_args()
        name = args["name"]
        isbn = args["isbn"]
        authors = args["authors"]
        country = args["country"]
        number_of_pages = args["number_of_pages"]
        publisher = args["publisher"]
        release_date = args["release_date"]

        response = []
        response_dict = {}
        data_dict = {}
        book_dict = {}
        author_list = []
        book_dict["name"] = name
        book_dict["isbn"] = isbn
        book_dict['authors'] = authors
        book_dict["number_of_pages"] = number_of_pages
        book_dict["publiser"] = publisher
        book_dict["country"] = country
        book_dict["release_date"] = release_date
        data_dict["book"] = book_dict
        response_dict["data"] = data_dict
        response_dict["status_code"] = 201
        response_dict["status"] = "success"

        # Save to Db
        save_book = Books(None, name, isbn, authors, country, number_of_pages, publisher, release_date, datetime.now(),
                          datetime.now())
        db.session.add(save_book)
        db.session.commit()
        return jsonify(response_dict)

    def get(self):
        """search a book by name, country, publisher or year. Input is in json format.
        If no input is there, it will return all the lists of books
        @name: string
        @country: string
        @publisher: string
        @year: integer
        :return: status code 200 on successful creation of a book record in database
        """
        print("Get Method")
        books = None
        try:
            data = request.json
            if 'name' in data:
                name = data['name']
                books = Books.query.filter_by(name=name).all()
            if 'country' in data:
                country = data['country']
                books = Books.query.filter_by(country=country).all()
            if 'publisher' in data:
                publisher = data['publisher']
                books = Books.query.filter_by(publisher=publisher).all()
            if 'year' in data:
                year = data['year']
                books = Books.query.filter(extract('year', Books.release_date) == year).all()
        except:
            books = Books.query.all()

        response_dict = {}
        data_list = []
        for book in books:
            book_dict = {}
            book_dict["id"] = book.id
            book_dict["name"] = book.name
            book_dict["isbn"] = book.isbn
            try:
                book_dict['authors'] = json.loads(book.authors)
            except:
                book_dict['authors'] = book.authors
            book_dict["number_of_pages"] = book.number_of_pages
            book_dict["publiser"] = book.publisher
            book_dict["country"] = book.country
            book_dict["release_date"] = book.release_date
            data_list.append(book_dict)
        response_dict["data"] = data_list
        response_dict["status_code"] = 200
        response_dict["status"] = "success"
        return jsonify(response_dict)