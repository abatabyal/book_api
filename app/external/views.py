from flask import (Blueprint, jsonify, request)
from .services import get_external_book_info

external_blueprint = Blueprint('external', __name__)

@external_blueprint.route('/api/external-books/', methods=['GET'])
def external():

    try:
        book_name = request.args.get('name')
        print(book_name)
    except:
        print('No Book Name entered in request')
        return jsonify({'book_name': book_name})

    response = get_external_book_info(book_name)
    return jsonify(response)