from pydub import AudioSegment
import json


transcription = open("translated_json.json")
data = json.load(transcription)


# Generate audio chunks and save them to temporary WAV files


def chop_initial_sound(input_file):

    audio = AudioSegment.from_file(input_file)

    print(len(audio))

    audio_clear = audio[10:]

    audio_clear.export(input_file,format='wav')
    

def remove_random_sound():
    for k in range(len(data)):
        chop_initial_sound(f"output_audio/translated_chunk{k}.wav")

