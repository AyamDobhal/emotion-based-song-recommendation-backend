import json
import os

from flask import Flask, request
from app.helpers.emotion_analysis import get_emotion

from app.helpers.lastfm import get_song

application = Flask(__name__)

app = application

if not os.path.exists("secrets.json"):
    raise Exception("Secrets file not found")

secrets = json.load(open("secrets.json"))

@app.route("/recommend", methods=["POST"])
def recommend():
    form = request.form
    emotion = get_emotion(form['text'])
    data = get_song(emotion, secrets["apiKey"])
    return data

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
