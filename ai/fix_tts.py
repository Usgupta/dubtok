from pydub import AudioSegment
import json
import os
import glob

files = glob.glob('/YOUR/PATH/*')
# Generate audio chunks and save them to temporary WAV files


def chop_initial_sound(input_file):

    audio = AudioSegment.from_file(input_file)

    audio_clear = audio[10:]

    audio_clear.export(input_file,format='wav')

def clear_chunks():
    files = glob.glob('../ai/chunks/*')
    for f in files:
        try: 
            os.remove(f)
        except:
            print(f'cant remove {f}')


def remove_random_sound():
    clear_chunks()
    transcription = open("../ai/translated_json.json")
    data = json.load(transcription)
    for k in range(len(data)):
        chop_initial_sound(f"../ai/output_audio/translated_chunk{k}.wav")

