import os
import time
import requests

def get_random_word():
    url = "https://wordsapiv1.p.rapidapi.com/words/"

    # TODO: Make querystring configurable from the command line
    querystring = {
        "random": "true",
        "letters": "8",
        "letterPattern": "^[A-z]+$"
    }

    headers = {
        # Get your API key at https://rapidapi.com/dpventures/api/wordsapi/pricing
        'x-rapidapi-key': os.environ['WORD_API'],
        'x-rapidapi-host': "wordsapiv1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    #print(response.text)
    return response.json()['word']

if __name__ == '__main__':

    print(get_random_word())