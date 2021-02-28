import requests
import os
from dotenv import load_dotenv

load_dotenv()
APIKEY = os.environ.get('APIKEY')


def find_subtitles(video_id):
    url = f"https://subtitles-for-youtube.p.rapidapi.com/subtitles/{video_id}"
    headers = {
        'x-rapidapi-key': APIKEY,
        'x-rapidapi-host': "subtitles-for-youtube.p.rapidapi.com"
        }
    params = {'lang':"EN"}
    
    response = requests.request("GET", url, headers=headers, params=params)
    return response.json()

def clean_subtitles(json_response):
    text = ''
    counter = 0 
    text_list = list()
    for index in json_response:
        if counter < 30 and index != json_response[-1]:    
            text += index['text']
            text += ' '
            counter += 1
        elif index == json_response[-1]:
            text += index['text']
            text += ' '
            text_list.append(text)
        
        else:
            text += index['text']
            text += ' '
            text_list.append(text) 
            counter = 0
            text = ''
    return text_list

