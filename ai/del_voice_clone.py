import requests
import os
from dotenv import load_dotenv

# voice_id = 's3://voice-cloning-zero-shot/7af03cba-0861-4713-a9b5-eb9afdb52038/cookie/manifest.json'

def del_vc(voice_id):

    load_dotenv()

    api_key = os.getenv("PLAYHT_APIKEY")
    user_id = os.getenv("PLAYHT_USERID")

    url = "https://api.play.ht/api/v2/cloned-voices/"

    payload = { "voice_id": voice_id }
    headers = {
    "Authorization": f"Bearer {api_key}",
    'X-USER-ID': f"{user_id}",
}

    response = requests.delete(url, json=payload, headers=headers)

    print(response.text)