import requests
from app.config import BOOK_URL
from datetime import datetime

def get_external_book_info(book_name):

    api_url = BOOK_URL + '?=' + book_name

    api_response = requests.get(api_url)
    print(api_response.text)
    response = {}
    book_data = {}
    data_list = []
    author_list = []
    json_api_response = api_response.json()
    if api_response.status_code == 200:
        response["status_code"] = 200
        response["status"] = "success"
        if json_api_response and 'name' in json_api_response[0]:
            book_data["name"] = json_api_response[0]["name"]
            book_data["isbn"] = json_api_response[0]["isbn"]
            author_list = [author for author in json_api_response[0]["authors"]]
            book_data["authors"] = author_list
            book_data["number_of_pages"] = json_api_response[0]["numberOfPages"]
            book_data["publisher"] = json_api_response[0]["publisher"]
            book_data["country"] = json_api_response[0]["country"]
            release_date = datetime.strptime(json_api_response[0]["released"], "%Y-%m-%dT%H:%M:%S").date()
            book_data["release_date"] = str(release_date)
            data_list.append(book_data)
        response["data"] = data_list
    return response
