import requests
import os
from dotenv import load_dotenv
# Define the API endpoint
url = "https://api.play.ht/api/v2/cloned-voices/instant"

load_dotenv()

# Define the API key (replace 'your_api_key' with your actual API key)
api_key = os.getenv("PLAYHT_APIKEY")
userid = os.getenv("PLAYHT_USERID")

print(userid)


# Define the headers
headers = {
    "Authorization": f"{api_key}",
    'X-USER-ID': f"{userid}",
}

def create_voice_clone(vocal_file):
# Define the file to upload and the voice name
    file_path = vocal_file
    voice_name = "cookie"

    # Create the files and data for the request
    files = {
        "sample_file": (file_path, open(file_path, "rb",), "audio/wav")
    }
    data = {
        "voice_name": voice_name
    }

    # Make the POST request to create the voice clone
    response = requests.post(url, headers=headers, files=files, data=data)

    # Check the response status
    if response.status_code == 201:
        print("Instant voice clone successfully created.")
        print("Response:", response.json())
        return response.json()['id']
        
    else:
        print(f"Failed to create voice clone. Status code: {response.status_code}")
        print("Response:", response.json())
    
