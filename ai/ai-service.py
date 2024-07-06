import demucs.separate
import transcribe
import translated_chunks
import voice_clone
import tts
import fix_tts
import sync_translation 

audio_file = "../cookie.mp4"

def preprocess(audio_file):

    # Separate the audio clip into vocals and no vocals
    demucs.separate.main(["--mp3", "--two-stems", "vocals", "-n", "mdx_extra", audio_file])

# preprocess(audio_file)

vocal_file = 'separated/mdx_extra/cookie/vocals.mp3'

# transcribe.transcribe(vocal_file)

# translated_chunks.create_translated_transcription(target_language='French')

voice_id = voice_clone.create_voice_clone(vocal_file)

tts.generate_tts(voice_id)

fix_tts.remove_random_sound()

sync_translation.sync_audio()





