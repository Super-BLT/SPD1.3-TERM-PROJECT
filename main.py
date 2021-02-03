from flask import Flask, make_response,send_file, render_template, request
from dotenv import load_dotenv
import os

load_dotenv()

APIKEY = os.environ.get("APIKEY")


app = Flask('__main__')

@app.route("/")
def homepage():
    return render_template('temp.html')

@app.route("/save/<url>",methods=["GET","POST"])
def saveurl(url):
    """Save Transcript Locally"""
    #makeApi Call with Url
    
    filename=f'{url}Transcript.txt'
    print(filename)
    if request.method == 'POST':
        new_file = open(filename,"x")
        new_file.write('Contents of API Call')
        new_file.close()
        return send_file(filename, as_attachment=True), os.remove(filename)
    
    return render_template('temp.html')
if __name__ == "__main__":
    app.run(debug=True)