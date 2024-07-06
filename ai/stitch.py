import os
from pydub import AudioSegment
import json

# novocals_audio_path = '../backend/separated/mdx_extra/cookie/no_vocals.mp3'


def translated_audio_track(novocals_audio_path, dubbed_audio_path):
    

    transcription = open("../ai/transcription.json")
    data = json.load(transcription)

    novocals_audio = AudioSegment.from_file(novocals_audio_path)

    for i,chunk in enumerate(data["segments"]):

        translated_chunk = AudioSegment.from_file(f'../ai/output_audio/sync_chunk{i}.wav')
        novocals_audio = novocals_audio.overlay(translated_chunk,position=chunk['start']*1000)
        novocals_audio.export(dubbed_audio_path, format="wav")

# translated_audio_track(novocals_audio_path)


