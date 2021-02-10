from flask import Flask, render_template,request
from dotenv import load_dotenv
import os

load_dotenv()

APIKEY = os.environ.get("APIKEY")


app = Flask('__main__')

@app.route("/")
def homepage():
    url = request.args.get("video-url")
    video_code = ''
    if url:
        split_url = url.split("?v=")
        video_code = split_url[1]
        
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)