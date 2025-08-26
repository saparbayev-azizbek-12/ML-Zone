import requests

FAST_API_URL = "https://spam-api-fmfe.onrender.com/"

def predict(text):
    payload = {"text": text}
    res = requests.post(FAST_API_URL, json=payload)

    if res.status_code == 200:
        return res.json()
    else:
        return {"status": False}