from unittest import TestCase
from app import app

class TestExternal(TestCase):
    def setUp(self):
       self.app = app
       self.client = self.app.test_client()

    #test with book name
    def test_ice_and_fire(self):
        response = self.client.get(path='/api/external-books?name=A Game of Thrones', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # test without book name
    def test_empty_book(self):
        response = self.client.get(path='/api/external-books?name=', follow_redirects=True)
        self.assertEqual(response.status_code, 400)