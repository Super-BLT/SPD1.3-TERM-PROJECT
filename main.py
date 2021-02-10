from flask import Flask
from dotenv import load_dotenv
import os
import requests

load_dotenv()

APIKEY = os.environ.get("APIKEY")


app = Flask('__main__')

@app.route("/")
def homepage():
    return "<h1>Welcome to uText! This project is a work in progress please check back later to experience the complete product.</h1>"

if __name__ == "__main__":
    app.run(debug=True)


@app.route("/lyrics")
def define():

    url = "https://subtitles-for-youtube.p.rapidapi.com/subtitles/_1y6bpdT3a4"

    querystring = {"translated":"Translated","type":"Human"}

    headers = {
        'x-rapidapi-key': "de9cc79eddmsh17f407668b65521p10b1ccjsn4736bfcc4d11",
        'x-rapidapi-host': "subtitles-for-youtube.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)