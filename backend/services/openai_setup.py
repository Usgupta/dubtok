import os
from dotenv import load_dotenv
from openai import OpenAI

# Gets the environment variable containing the API key and sets up the OpenAI client
def setup_openai():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key is None:
        print("Please add your OpenAI API key to an environment file.")
        return
    return OpenAI(api_key=api_key)
