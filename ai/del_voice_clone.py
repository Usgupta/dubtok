import requests
import os
from dotenv import load_dotenv

# voice_id = 's3://voice-cloning-zero-shot/8510399a-5178-48e9-b4a6-ffeb6b3333d1/cookie/manifest.json'
def get_voice_id():

    load_dotenv()

    api_key = os.getenv("PLAYHT_APIKEY")
    user_id = os.getenv("PLAYHT_USERID")

    url = "https://api.play.ht/api/v2/cloned-voices"

    headers = {
        "accept": "application/json",
       "Authorization": f"Bearer {api_key}",
       'X-USER-ID': f"{user_id}",
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print("Response:", response.json())
        if len(response.json())!=0:
            return response.json()[0]['id']
        else:
            return
        
    else:
        return 
        print("Response:", response.json())

    


def del_vc():

    voice_id = get_voice_id()

    if voice_id==None:
        # raise Exception("no voice id found")
        return

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

    print('voice clone deleted')

    print(response.text)
# del_vc(voice_id)