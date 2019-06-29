import json
from unittest import TestCase
from app import app

class TestInternalUpdates(TestCase):

    def setUp(self):
       self.app = app
       self.client = self.app.test_client()

    # update book negative without form data
    def test_update_negative_no_data(self):
       response = self.client.patch(path='/api/v1/books/22')
       self.assertEqual(response.status_code, 400)

    # update book negative with string
    def test_update_negative_string(self):
       response = self.client.patch(path='/api/v1/books/thirteen')
       self.assertEqual(response.status_code, 404)

    # update book negative by empty form
    def test_negative_empty_form(self):
       response = self.client.patch(path='/api/v1/books/22', data=dict())
       self.assertEqual(response.status_code, 400)

    # update book negative by empty name
    def test_negative_update_name(self):
       response = self.client.patch(path='/api/v1/books/22', data=dict(name = ""))
       self.assertEqual(response.status_code, 400)

    # update book negative by empty isbn
    def test_update_negative_isbn(self):
       response = self.client.patch(path='/api/v1/books/22', data=dict(isbn = ""))
       self.assertEqual(response.status_code, 400)

    # update book negative by empty authors
    def test_update_negative_authors(self):
       response = self.client.patch(path='/api/v1/books/22', data=dict(authors = []))
       self.assertEqual(response.status_code, 400)

    # update book negative by empty country
    def test_update_negative_country(self):
       response = self.client.patch(path='/api/v1/books/22', data=dict(country = ''))
       self.assertEqual(response.status_code, 400)

    # update book negative by empty number_of_pages
    def test_update_negative_number_of_pages_zero(self):
       response = self.client.patch(path='/api/v1/books/22', data=dict(number_of_pages = 0))
       self.assertEqual(response.status_code, 400)

    # update book negative by empty number_of_pages
    def test_update_negative_number_of_pages_negative(self):
       response = self.client.patch(path='/api/v1/books/22', data=dict(number_of_pages = -2))
       self.assertEqual(response.status_code, 400)

    # update book negative by empty publisher
    def test_update_negative_publisher(self):
       response = self.client.patch(path='/api/v1/books/22', data=dict(publisher = ''))
       self.assertEqual(response.status_code, 400)

    # update book negative by wrong release date
    def test_update_negative_wrong_release_date(self):
       response = self.client.patch(path='/api/v1/books/22', data=dict(release_date = '9'))
       self.assertEqual(response.status_code, 400)

    # update book negative by empty release date
    def test_update_negative_empty_release_date(self):
       response = self.client.patch(path='/api/v1/books/22', data=dict(release_date = ''))
       self.assertEqual(response.status_code, 400)

    # update book negative by wrong parameter
    def test_update_negative_empty_release_date(self):
       response = self.client.patch(path='/api/v1/books/22', data=dict(id = 1))
       self.assertEqual(response.status_code, 400)

    # update book by name
    def test_update_name(self):
       response = self.client.patch(path='/api/v1/books/22', data=dict(name = "The Adventures of Sherlock Holmes"))
       self.assertEqual(response.json['status_code'], 200)

    # update book by isbn
    def test_update_isbn(self):
       response = self.client.patch(path='/api/v1/books/22', data=dict(isbn = "123456789"))
       self.assertEqual(response.json['status_code'], 200)

    # update book by authors
    def test_update_authors(self):
       response = self.client.patch(path='/api/v1/books/22', data=dict(authors = ["Bruce Wayne", "Tony Stark"]))
       self.assertEqual(response.json['status_code'], 200)

    # update book by authors
    def test_update_authors(self):
       response = self.client.patch(path='/api/v1/books/22', data=dict(authors = ["Tommy Lee Wayne"]))
       self.assertEqual(response.json['status_code'], 200)

    # update book by country
    def test_update_country(self):
       response = self.client.patch(path='/api/v1/books/22', data=dict(country = 'India'))
       self.assertEqual(response.json['status_code'], 200)

    # update book by number_of_pages
    def test_update_number_of_pages(self):
       response = self.client.patch(path='/api/v1/books/22', data=dict(number_of_pages = 999))
       self.assertEqual(response.json['status_code'], 200)

    # update book by publisher
    def test_update_publisher(self):
       response = self.client.patch(path='/api/v1/books/22', data=dict(publisher = 'Penguin Classics'))
       self.assertEqual(response.json['status_code'], 200)

    # update book by release date
    def test_update_release_date(self):
       response = self.client.patch(path='/api/v1/books/22', data=dict(release_date = '2019-06-29'))
       self.assertEqual(response.json['status_code'], 200)

    # search book negative without id
    def test_search_book_negative(self):
       response = self.client.get(path='/api/v1/books/')
       self.assertEqual(response.status_code, 404)

    # search book negative with string
    def test_search_book_negative_string(self):
       response = self.client.get(path='/api/v1/books/abcd')
       self.assertEqual(response.status_code, 404)

    # search book positive
    def test_search_book_positive(self):
       response = self.client.get(path='/api/v1/books/22')
       self.assertEqual(response.json['status_code'], 200)

    # search book positive not exist
    def test_search_book_positive_not_exist(self):
       response = self.client.get(path='/api/v1/books/189')
       self.assertEqual(response.status_code, 404)

    # delete book not exist
    def test_delete_book_not_exist(self):
       response = self.client.delete(path='/api/v1/books/189')
       self.assertEqual(response.status_code, 404)

    # delete book negative without id
    def test_delete_book_negative(self):
       response = self.client.delete(path='/api/v1/books/')
       self.assertEqual(response.status_code, 404)

    # delete book negative with string
    def test_delete_book_negative_string(self):
       response = self.client.delete(path='/api/v1/books/twelve')
       self.assertEqual(response.status_code, 404)

    # delete book positive
    def test_delete_book_positive(self):
       response = self.client.delete(path='/api/v1/books/43')
       self.assertEqual(response.json['status_code'], 200)