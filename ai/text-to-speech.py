import os
import time
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set your PlayHT credentials
USER_ID = os.getenv("PLAYHT_USERID")
API_KEY = os.getenv("PLAYHT_APIKEY")

# API endpoint for creating a TTS job
TTS_ENDPOINT = "https://api.play.ht/api/v2/tts"

# Headers for the request
headers = {
    "Authorization": f"Bearer {API_KEY}",
    'X-USER-ID':USER_ID,
    "Content-Type": "application/json",
    "accept": "application/json"
}

# Data for the request
data = {
    "text": "Pouvez-vous me donner l'email de votre compte ou votre numéro de téléphone ?",
    "voice": "s3://voice-cloning-zero-shot/d9ff78ba-d016-47f6-b0ef-dd630f59414e/female-cs/manifest.json",
    "output_format": "mp3",
    "sample_rate": 22050
}

# Make the request to create a TTS job
response = requests.post(TTS_ENDPOINT, json=data, headers=headers)

if response.status_code == 201:
    # Job created successfully
    job_id = response.json()["id"]
    print(f"TTS job created with ID: {job_id}")

    # URL to get job status
    job_status_url = f"{TTS_ENDPOINT}/{job_id}"

    # Poll the job status until it's completed
    while True:
        status_response = requests.get(job_status_url, headers=headers)
        status_data = status_response.json()

        if status_data["status"] == "completed":
            audio_url = status_data["output"]["url"]
            print(f"Audio generated. Download it from: {audio_url}")
            break
        elif status_data["status"] == "failed":
            print("TTS job failed.")
            break
        else:
            print("TTS job is still in progress...")
            time.sleep(5)  # Wait for 5 seconds before checking again

    # Download the audio file
    audio_response = requests.get(audio_url)

    # Save the audio file
    with open("output.mp3", "wb") as audio_file:
        audio_file.write(audio_response.content)

    print("Audio file saved as output.mp3")
else:
    print(f"Failed to create TTS job. Status code: {response.status_code}")
    print(response.json())
