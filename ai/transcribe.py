from ai.openai_setup import setup_openai
import json
import os

def transcribe(audio_file):

  # Load the environment file and setup OpenAI client
  client = setup_openai() 
  audio_file = open(audio_file, "rb")
  # audio_file = open("../Umang.mp3","rb")
  # Begin transcribing
  transcript = client.audio.transcriptions.create(
    file=audio_file,
    model="whisper-1",
    response_format="verbose_json",
    timestamp_granularities=["segment"]
    )
  
  BASE_DIR = os.path.dirname(os.path.abspath(__file__))

  print(BASE_DIR)

  file_path = os.path.join(BASE_DIR, "..", "ai", "transcription.json")

  # Convert the transcript to a dictionary
  transcript_dict = transcript.to_dict()
  # Save the entire JSON response
  with open(file_path, "w") as json_file:
      json.dump(transcript_dict, json_file, indent=4)
