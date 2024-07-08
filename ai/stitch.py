import os
from pydub import AudioSegment
import json

# novocals_audio_path = '../backend/separated/mdx_extra/cookie/no_vocals.mp3'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def translated_audio_track(novocals_audio_path, dubbed_audio_path):
    
    transcription_file_path = os.path.join(BASE_DIR, "..", "ai", "transcription.json")

    transcription = open(transcription_file_path)
    data = json.load(transcription)

    novocals_audio = AudioSegment.from_file(novocals_audio_path)

    for i,chunk in enumerate(data["segments"]):
        sync_chunk_path = os.path.join(BASE_DIR, "..", "ai", f"output_audio/sync_chunk{i}.wav")
        translated_chunk = AudioSegment.from_file(sync_chunk_path)
        novocals_audio = novocals_audio.overlay(translated_chunk,position=chunk['start']*1000)
        novocals_audio.export(dubbed_audio_path, format="wav")

# translated_audio_track(novocals_audio_path)


