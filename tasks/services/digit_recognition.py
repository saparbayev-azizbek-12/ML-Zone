import requests

FAST_API_URL = "https://digit-recognizer-api.onrender.com"

def predict(arr):
    payload = {"array": arr}
    res = requests.post(FAST_API_URL, json=payload)
    print("Response:", res)

    if res.status_code == 200:
        return res.json()
    else:
        return {"status": False, "message": res.text}