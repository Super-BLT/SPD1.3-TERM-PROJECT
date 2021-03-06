from flask import Flask, make_response,send_file, render_template, request
from API import find_subtitles, clean_subtitles
from dotenv import load_dotenv
import os

load_dotenv()

APIKEY = os.environ.get("APIKEY")


app = Flask(__name__)

@app.route("/")
def homepage():
    url = request.args.get("video-url")
    video_code = ''
    context = {
        'captions':'',
        'video_url':'',
        'video_code':''
    }
    if url:
        split_url = url.split("?v=")
        video_code = split_url[1]
        captions_dirty = find_subtitles(video_code)
        captions_clean = clean_subtitles(captions_dirty)
        context['captions'] = captions_clean
        context['video_url'] = url
        context['video_code'] = video_code
    
    return render_template('index.html',**context)

@app.route("/save",methods=["GET","POST"])
def saveurl():
    """Save Transcript Locally"""
    

    
    if request.method == 'POST':
        url = request.form.get("video-url")
        video_code = ''
        if url:
            split_url = url.split("?v=")
            video_code = split_url[1]
        filename=f'{video_code}Transcript.txt'
        captions= clean_subtitles(find_subtitles(video_code))
        new_file = open(filename,"x")
        for text in captions:
            new_file.writelines(text)
        new_file.close()
        return send_file(filename, as_attachment=True), os.remove(filename)
    
    return render_template('temp.html')
if __name__ == "__main__":
    app.run(debug=True)