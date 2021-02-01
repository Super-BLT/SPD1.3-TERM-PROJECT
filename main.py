from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

APIKEY = os.environ.get("APIKEY")


app = Flask('__main__')

@app.route("/")
def homepage():
    return APIKEY

if __name__ == "__main__":
    app.run(debug=True)