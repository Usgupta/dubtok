import demucs.separate
import ai.transcribe as transcribe
import ai.translated_chunks as translated_chunks
import ai.voice_clone as voice_clone
import ai.tts as tts
import ai.fix_tts as fix_tts
import ai.sync_translation as sync_translation
import ai.del_voice_clone as delvc
from ai.stitch import translated_audio_track
import ai.newtest as newtest
from pydub import AudioSegment
import io
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# audio_file = "../cookie.mp4"

def save_file_object_as_mp3(file_object, output_file_path):
    # Read the audio data from the file object
    file_object.seek(0)  # Ensure the file pointer is at the beginning
    audio_data = file_object.read()

    # Load the audio data into an AudioSegment
    audio_segment = AudioSegment.from_file(io.BytesIO(audio_data), format="wav")

    # Export the audio segment as an MP3 file
    audio_segment.export(output_file_path, format="mp3")

    print(f"File saved as {output_file_path}")

    return output_file_path


def preprocess(audio_file):

    # Separate the audio clip into vocals and no vocals
    demucs.separate.main(["--mp3", "--two-stems", "vocals", "-n", "mdx_extra", audio_file])

def dubbing(file_path, dub_type, filename):

    # newtest.new()
    preprocess(file_path)

    vocal_file = f'separated/mdx_extra/{filename}/vocals.mp3'

    novocal_file = f'separated/mdx_extra/{filename}/no_vocals.mp3' 

    dubbed_audio_path = os.path.join(BASE_DIR, "..", "ai", f"output_audio/translated_final.mp3")

    transcribe.transcribe(vocal_file)

    translated_chunks.create_translated_transcription(target_language=dub_type)

    delvc.del_vc()

    voice_id = voice_clone.create_voice_clone(vocal_file)

    # print("VOICE ID------", voice_id)

    tts.generate_tts(voice_id)

    fix_tts.remove_random_sound()

    sync_translation.sync_audio()

    delvc.del_vc()

    translated_audio_track(novocal_file, dubbed_audio_path)

    return dubbed_audio_path







