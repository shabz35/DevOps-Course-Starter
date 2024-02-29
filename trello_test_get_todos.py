import dotenv

import os
import requests
dotenv.load_dotenv()

reqUrl = "https://api.trello.com/1/boards/65afd1d3a662c6c7228ce261/lists"

query_parameters =  {
    "key": os.getenv("TRELLO_API_KEY"),
    "token": os.getenv("TRELLO_API_TOKEN"),
    "cards": "open",
    "card_fields":"id,name"
}


response = requests.get(reqUrl, params= query_parameters)

print(response.text)