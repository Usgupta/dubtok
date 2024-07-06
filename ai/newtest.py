import os
import json 
import wave 
import tempfile
from pydub import AudioSegment

def newshit():

    transcription = open("../ai/translated_json.json")
    data = json.load(transcription)

    audio = AudioSegment.from_file("../ai/output_audio/translated_chunk0.wav")

    # with tempfile.TemporaryDirectory() as tmpdirname:
    #     tmpdirname = "../ai/chunks/"

    #     chunk_file = os.path.join(tmpdirname, f"chunk_0.wav")
    #     with wave.open(chunk_file, 'wb') as wave_file:
    #         print('yessss fuck off')