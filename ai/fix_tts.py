from pydub import AudioSegment
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def chop_initial_sound(input_file):
    audio = AudioSegment.from_file(input_file)
    audio_clear = audio[10:]
    audio_clear.export(input_file,format='wav')

def remove_random_sound():
    translation_file_path = os.path.join(BASE_DIR, "..", "ai", "translated_json.json")

    transcription = open(translation_file_path)
    data = json.load(transcription)
    for k in range(len(data)):
        trans_chunk_path = os.path.join(BASE_DIR, "..", "ai", f"output_audio/translated_chunk{k}.wav")
        chop_initial_sound(trans_chunk_path)

