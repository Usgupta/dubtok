from openai_setup import setup_openai
import json

# Load the environment file and setup OpenAI client
client = setup_openai() 
audio_file = open("../sample_videos/sample2.mp4", "rb")

# Begin transcribing
transcript = client.audio.transcriptions.create(
  file=audio_file,
  model="whisper-1",
  response_format="verbose_json",
  timestamp_granularities=["word"]
)

# Convert the transcript to a dictionary
transcript_dict = transcript.to_dict()

# Save the entire JSON response
with open("../ai/transcription.json", "w") as json_file:
    json.dump(transcript_dict, json_file, indent=4)
