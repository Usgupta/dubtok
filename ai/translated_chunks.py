import json
from ai.openai_setup import setup_openai
import os

# Load the environment file and setup OpenAI client
client = setup_openai()

# message = "你妈妈没有毛"
# target_language = "French"



def create_translated_transcription(target_language):
  BASE_DIR = os.path.dirname(os.path.abspath(__file__))

  transcription_file_path = os.path.join(BASE_DIR, "..", "ai", "transcription.json")

  transcription = open(transcription_file_path)
  data = json.load(transcription)
  translated_json = []

  for chunk in data["segments"]:
    
    # print(chunk['text'])
    # print(translate(chunk['text']))
    translated_item = {"orignal": chunk['text'],
                       "translated": translate(chunk['text'], target_language),
                       "duration": chunk['end']-chunk['start'] }
    
    translated_json.append(translated_item)

  translation_file_path = os.path.join(BASE_DIR, "..", "ai", "translated_json.json")

  with open(translation_file_path, "w", encoding="utf-8") as json_file:
        json.dump(translated_json, json_file, indent=4, ensure_ascii=False)


def translate(message, target_language):
  # Translate the message
  completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
      {"role": "system", "content": "Translate user message to the target language the user specifies before the message. Return only the translated text."},
      {"role": "user", "content": target_language + ":" + message}
    ]
  )

  print(completion.choices[0].message)

  return completion.choices[0].message.content




