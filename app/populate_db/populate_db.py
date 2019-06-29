import requests
import json
from app.config import BOOK_URL
from datetime import datetime
from app.models.books import Books
from app import db

def populate_db():
    """
    Standaone utility to populate database from Ice And Fire API for testing
    :return: inserts records to database
    """

    api_url = BOOK_URL

    api_response = requests.get(api_url)
    print(api_response.text)
    json_api_response = api_response.json()
    if api_response.status_code == 200:
        for book in json_api_response:
            name = book['name']
            isbn = book["isbn"]
            authors = json.dumps(book["authors"])
            country = book['country']
            number_of_pages = int(book["numberOfPages"])
            publisher = book["publisher"]
            release_date = datetime.strptime(book["released"], "%Y-%m-%dT%H:%M:%S").date()

            book_insert = Books(None, name, isbn, authors, country, number_of_pages, publisher, release_date, datetime.now(),
            datetime.now())
            db.session.add(book_insert)
            db.session.commit()

populate_db()