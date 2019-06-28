#Ice and Fire API
BOOK_URL = 'https://www.anapioficeandfire.com/api/books'

#MySQL DB
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = '123456'
MYSQL_DB = 'book_api'
MYSQL_CURSORCLASS = 'DictCursor'
# sqlalchemy connection string
SQLALCHEMY_DATABASE_URI = 'mysql://'+MYSQL_USER+':'+MYSQL_PASSWORD+'@'+MYSQL_HOST+'/'+MYSQL_DB