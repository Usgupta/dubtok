from pydub import AudioSegment
from audiostretchy.stretch import stretch_audio
import json
from scipy.io import wavfile
import librosa, numpy as np

def sync(input_file, output_file, target_duration):

    song, fs = librosa.load(input_file)

    synced_audio = librosa.effects.time_stretch(song, 1.2816082687941117)

    scipy.io.wavfile.write(output_file, fs, sync_audio) # save the song

def sync_audio(input_file, output_file, target_duration):
    audio = AudioSegment.from_file(input_file)
    initial_duration = len(audio)
    ratio = (1000*target_duration)/len(audio)
    stretch_audio(input_file, output_file, ratio=ratio)
    output_audio = AudioSegment.from_file(output_file)
    final_duration = len(output_audio)
    print('\n initial ratio was ', ratio, ' actual is ', len(output_audio)/len(audio), 'the durations are: ', initial_duration, ' ', final_duration, ' ', target_duration)




translated_json  = open("translated_json.json")
translated_chunks = json.load(translated_json)

combined = AudioSegment.empty()
# Generate audio chunks and save them to temporary WAV files

for k in range(len(translated_chunks)):
        # Example usage:
    input_file = f"output_audio/translated_chunk{k}.wav"
    output_file = f"output_audio/sync_chunk{k}.wav"
    target_duration = translated_chunks[k]["duration"]  # Target duration in seconds
    # print(target_duration)

    sync(input_file,output_file,target_duration)

    # sync_audio(input_file,output_file,target_duration)
    combined+=AudioSegment.from_file(output_file)

combined.export('output_audio/full_translated.wav',format='wav')
print('saved translation')



