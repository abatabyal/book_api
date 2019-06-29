from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

#mysql = MySQL(app)

from flask_restful import Api
from app.internal.BookAPI import BookAPI
from app.internal.UpdateBookAPI import UpdateBookAPI
from app.external.ExternalAPI import ExternalAPI
api = Api(app)

#Flask REST API End points
api.add_resource(ExternalAPI, '/api/external-books')
api.add_resource(BookAPI, '/api/v1/books')
api.add_resource(UpdateBookAPI, '/api/v1/books/<int:id>')