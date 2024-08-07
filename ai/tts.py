
from pyht import Client
from dotenv import load_dotenv
from pyht.client import TTSOptions
import os
from pydub import AudioSegment
import wave
import tempfile
import json
import time

load_dotenv()

# Generate audio chunks and save them to temporary WAV files

def generate_tts(voice_id):
    apik = os.getenv("PLAYHT_APIKEY")
    client = Client(user_id = os.getenv("PLAYHT_USERID"),api_key = f"Bearer {apik}")

  
  	# for on-prem users, uncomment and add the advanced grpc_addr option below. Replace grpc_addr with your endpoint. 
  	# advanced=client.Client
    # .AdvancedOptions(grpc_addr="{your-endpoint}.on-prem.play.ht:11045")
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    translation_file_path = os.path.join(BASE_DIR, "..", "ai", "translated_json.json")

    audio_segs = []
    transcription = open(translation_file_path, encoding='utf-8')
    data = json.load(transcription)

    # List to store audio chunks

    audio_chunks = []
    

    # voice_id = "s3://voice-cloning-zero-shot/8a9188ec-16d5-4e97-a328-fde0ec35a611/umang/manifest.json"

    options = TTSOptions(voice=voice_id,)

    for k in range(len(data)):
      

        print(data[k]["translated"])

        try:

            with tempfile.TemporaryDirectory() as tmpdirname:
                tmpdirname = "../ai/chunks/"
                for i, chunk in enumerate(client.tts(data[k]["translated"], options)):

                    # print(chunk)
                    # print(type(chunk))

                    # with open(f'chunks/myfile{k}.wav', mode='bx') as f:
                    #     f.write(chunk)
                    
                    chunk_file = os.path.join(BASE_DIR,tmpdirname, f"chunk_{i}.wav")
                    with wave.open(chunk_file, 'wb') as wave_file:
                        wave_file.setnchannels(1)  # mono audio
                        wave_file.setsampwidth(2)  # 16-bit audio
                        wave_file.setframerate(22050)  # sample rate
                        wave_file.writeframes(chunk)
                    audio_chunks.append(chunk_file)


                combined = AudioSegment.empty()
                for chunk_file in audio_chunks:
                    chunk_audio = AudioSegment.from_wav(chunk_file)
                    combined += chunk_audio

                # Export the combined audio segment to a WAV file
                chunk_path = os.path.join(BASE_DIR, "..", "ai", f"output_audio/translated_chunk{k}.wav")
                combined.export(chunk_path, format="wav")

                audio_chunks = []

                print(f"Audio saved to translated_chunk{k}.wav")

            time.sleep(1)

        except Exception as e:
            print(f"Error processing item {k}: {e}")
            continue
    
    print(f"\n Translated chunks all complete")
    

# print(audio_chunks)
    

    



