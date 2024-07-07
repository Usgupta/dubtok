from pydub import AudioSegment
import json

def chop_initial_sound(input_file):
    audio = AudioSegment.from_file(input_file)
    audio_clear = audio[10:]
    audio_clear.export(input_file,format='wav')

def remove_random_sound():
    transcription = open("../ai/translated_json.json")
    data = json.load(transcription)
    for k in range(len(data)):
        chop_initial_sound(f"../ai/output_audio/translated_chunk{k}.wav")

