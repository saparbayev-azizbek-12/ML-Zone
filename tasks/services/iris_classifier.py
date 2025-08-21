import requests

FAST_API_URL = "https://iris-api-7agz.onrender.com/"

def predict(arr):
    payload = {"array": arr}
    res = requests.post(FAST_API_URL, json=payload)

    if res.status_code == 200:
        return res.json()
    else:
        return {"status": False}