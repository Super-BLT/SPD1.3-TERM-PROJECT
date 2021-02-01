from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

APIKEY = os.environ.get("APIKEY")


app = Flask('__main__')

@app.route("/")
def homepage():
    return "<h1>Welcome to uText! This project is a work in progress please check back later to experience the complete product.</h1>"

if __name__ == "__main__":
    app.run(debug=True)