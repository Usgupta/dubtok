from openai_setup import setup_openai


message = "你妈妈没有毛"
target_language = "French"

def translate(message):
  # Load the environment file and setup OpenAI client
  client = setup_openai()

  # Translate the message
  completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
      {"role": "system", "content": "Translate user message to the target language the user specifies before the message. Return only the translated text without spaces in the beginning"},
      {"role": "user", "content": target_language + ":" + message}
    ]
  )

  print(completion.choices[0].message)

  return completion.choices[0].message