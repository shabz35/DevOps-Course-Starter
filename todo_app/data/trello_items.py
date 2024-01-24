import os
import requests

def get_items():
    pass


def add_item(title):
    
    req_url = "https://api.trello.com/1/cards"

    query_parameters =  {
        "key": os.getenv("TRELLO_API_KEY"),
        "token": os.getenv("TRELLO_API_TOKEN"),
        "name": title,
        "idList": os.getenv("TRELLO_TODO_TODO_LIST_ID")
    }

    response = requests.post(req_url, params = query_parameters)

    print(response.text)