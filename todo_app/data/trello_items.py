import os
import requests

from todo_app.data.item import Item

def get_items():
    reqUrl = "https://api.trello.com/1/boards/65afd1d3a662c6c7228ce261/lists"

    query_parameters =  {
        "key": os.getenv("TRELLO_API_KEY"),
        "token": os.getenv("TRELLO_API_TOKEN"),
        "cards": "open",
        "card_fields":"id,name"
    }


    response = requests.get(reqUrl, params= query_parameters)

    response_json = response.json()

    cards = []
    for trello_list in response_json:
        for card in trello_list['cards']:
            item = Item.from_trello_card(card, trello_list)
            cards.append(item)

    print(cards)
    return cards


def add_item(title):
    
    req_url = "https://api.trello.com/1/cards"

    query_parameters =  {
        "key": os.getenv("TRELLO_API_KEY"),
        "token": os.getenv("TRELLO_API_TOKEN"),
        "name": title,
        "idList": os.getenv("TRELLO_TODO_LIST_ID")
    }

    response = requests.post(req_url, params = query_parameters)

    print(response.text)


def move_item_to_done(item_id):
    reqUrl = f"https://api.trello.com/1/cards/{item_id}"

    query_parameters =  {
        "key": os.getenv("TRELLO_API_KEY"),
        "token": os.getenv("TRELLO_API_TOKEN"),
        "idList": os.getenv("TRELLO_DONE_LIST_ID")
    }

    response = requests.put(reqUrl, params= query_parameters)
    print(response.text)
    