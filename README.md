Environment:

Ubuntu 16.04, Python 3.7, MySQL 8.0

1. create mysql db named 'mstakx' with user 'root' and password '123456' as used in config.py. The db structure is under
 the directory db_struct/mstakx.sql. It contains the structure of table books. The table can be populated using the 
 standalone utility app/populate_db/populate_db.py. It saves the results from Ice and Fire API.

2. create the virtual environment and install requirements using:
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python3 run.py 
    
3. The unit tests are under /app/tests. 

4. Code coverage report is done with nose and unittest module using the following command from Ubuntu terminal:
venv/bin/nosetests --with-coverage --cover-package=app.internal --cover-package=app.external --cover-erase --cover-html 
--cover-inclusive app/tests/test_update_book_api.py app/tests/test_book_api.py app/tests/test_external_api.py 

5. The HTML report is saved under the directory cover. It can be accessed by index.html.

