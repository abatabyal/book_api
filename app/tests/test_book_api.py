import json
from unittest import TestCase
from app import app

class TestInternal(TestCase):

    def setUp(self):
       self.app = app
       self.client = self.app.test_client()

    #create book
    def test_create_positive(self):
        """Positive unit test case for creating a book record
        :return:
        """
        response = self.client.post(path='/api/v1/books', data=json.dumps({
            "name": "My Test Book 33",
            "isbn": "123-3213243567",
            "authors":[
                "John Doe",
                "Arindam Batabyal"
            ],
            "country":"United States",
            "number_of_pages": "234",
            "publisher": "Acme Books",
            "release_date":"2019-08-17"
            }), content_type='application/json')
        self.assertEqual(response.json['status_code'], 201)

    # create book negative parameter missing
    def test_create_negative_missing_params(self):
        """Negative unit test case for creating a book record with missing name
        :return:
        """
        response = self.client.post(path='/api/v1/books', data=json.dumps({

            "isbn": "123-3213243567",
            "authors": [
                "John Doe",
                "Arindam Batabyal"
            ],
            "country": "United States",
            "number_of_pages": "234",
            "publisher": "Acme Books",
            "release_date": "2019-08-17"
        }), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    # create book negative parameter empty
    def test_create_negative_empty_params(self):
        """Negative unit test case for creating a book record with empty country
        :return:
        """
        response = self.client.post(path='/api/v1/books', data=json.dumps({
            "name": "My Test Book 33",
            "isbn": "123-3213243567",
            "authors": [
                "John Doe",
                "Arindam Batabyal"
            ],
            "country": "",
            "number_of_pages": "234",
            "publisher": "Acme Books",
            "release_date": "2019-08-17"
        }), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    # positive testing get book list all
    def test_get_book_list(self):
        response = self.client.get(path='/api/v1/books')
        self.assertEqual(response.json['status_code'], 200)

    # positive testing get book list by name
    def test_get_book_name(self):
        response = self.client.get(path='/api/v1/books', data=json.dumps({"name": "My Test Book 33"}),
                                                             content_type='application/json')
        self.assertEqual(response.json['status_code'], 200)

    # positive testing get book list by country
    def test_get_book_country(self):
        response = self.client.get(path='/api/v1/books', data=json.dumps({"country": "United States"}),
                                   content_type='application/json')
        self.assertEqual(response.json['status_code'], 200)

    # positive testing get book list by publisher
    def test_get_book_publisher(self):
        response = self.client.get(path='/api/v1/books', data=json.dumps({"publisher": "Acme Books"}),
                                   content_type='application/json')
        self.assertEqual(response.json['status_code'], 200)

    # positive testing get book list by year
    def test_get_book_year(self):
        response = self.client.get(path='/api/v1/books', data=json.dumps({"year": "1999"}),
                                   content_type='application/json')
        self.assertEqual(response.json['status_code'], 200)

    # negative testing get book list by isbn not allowed
    def test_get_book_isbn(self):
        response = self.client.get(path='/api/v1/books', data=json.dumps({"isbn": "123456789"}),
                                   content_type='application/json')
        self.assertEqual(response.json['status_code'], 400)