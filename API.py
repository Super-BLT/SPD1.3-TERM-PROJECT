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
    for index in json_response:
       text += index['text']
       text += ' '
    return text

