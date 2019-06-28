from app import db

class Books(db.Model):
    """docstring for Books"""
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    isbn = db.Column(db.String(15))
    authors = db.Column(db.JSON)
    country = db.Column(db.String(40))
    number_of_pages = db.Column(db.Integer)
    publisher = db.Column(db.String(100))
    release_date = db.Column(db.Date)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __init__(self, id, name, isbn, authors, country, number_of_pages, publisher, release_date,
                 created_at, updated_at):
        self.id = id
        self.name = name
        self. isbn = isbn
        self.authors = authors
        self.country = country
        self.number_of_pages = number_of_pages
        self.publisher = publisher
        self.release_date = release_date
        self.created_at = created_at
        self.updated_at = updated_at
