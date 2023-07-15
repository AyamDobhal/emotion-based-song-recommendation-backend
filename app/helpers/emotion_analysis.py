import skops.io as sio
import os

if not os.path.exists('emotion-detection/model.skops'):
    raise Exception("Model not found")

model = sio.load('emotion-detection/model.skops', trusted=True)

def get_emotion(text: str) -> str:
    return model.predict([text])[0]
