import os

import skops.io as sio

if not os.path.exists("emotion-detection/model.skops"):
    raise Exception("Model not found")

model = sio.load("emotion-detection/model.skops", trusted=True)


def get_emotion(text: str) -> str:
    """
    Get emotion from text
    """
    return model.predict([text])[0]
