import requests
import time
from typing import List
from dotenv import dotenv_values

API_URL = 'https://api.telegram.org/bot'
ENV = dotenv_values('.env')
BOT_TOKEN = ENV['BOT_TOKEN']
TEXT = 'This is cool update!'
MAX_COUNTER = 50


offset = -2
counter = 0
chat_id: int
timeout = 60
updates: dict



def do_something() -> None:
    print('It`s update')

def cat_send() -> str:
    cat_response: requests.Response
    cat_link: str
    API_CAT = 'https://api.thecatapi.com/v1/images/search'
    ERROR_TEXT = 'Здесь должна была быть картинка с котиком :('
    cat_response = requests.get(API_CAT)
    if cat_response.status_code == 200:
        cat_link = cat_response.json()[0]['url']
        return 'Photo', 'photo', cat_link
    else:
        return 'Message', 'text', ERROR_TEXT


while True:
    start_time = time.time()
    UPD = f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}&timeout={timeout}'
    updates = requests.get(UPD).json()
    #print(updates)
    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            do_something()
            chat_id = result['message']['from']['id']
            send, types, content = cat_send()
            requests.get(f'{API_URL}{BOT_TOKEN}/send{send}?chat_id={chat_id}&{types}={content}')

    time.sleep(1)
    end_time = time.time()
    print(f"Time for requests to Telegram API: {end_time-start_time}")
