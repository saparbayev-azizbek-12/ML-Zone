import requests

FAST_API_URL = "http://127.0.0.1:8000/"

def predict(text):
    payload = {"text": text}
    res = requests.post(FAST_API_URL, json=payload)

    if res.status_code == 200:
        return res.json()
    else:
        return {"status": False}