import ffmpeg
import math
import json
from pydub import AudioSegment


def adjust_audio_duration(input_file, output_file, target_duration_seconds):
    # Get the duration of the input audio file using ffprobe
    try:
        probe = ffmpeg.probe(input_file)
        audio_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'audio'), None)
        if audio_stream is None:
            raise ValueError(f"No audio stream found in {input_file}")
        duration = float(audio_stream['duration'])

        # Calculate the speed ratio to adjust the duration
        current_duration = duration
        if current_duration <= 0:
            raise ValueError(f"Invalid duration {current_duration} for {input_file}")
        speed_ratio = target_duration_seconds / current_duration

        # Calculate the speed factor to pass to ffmpeg
        # Speed factor 1.0 is normal speed, <1.0 is slower, >1.0 is faster
        speed_factor = 1.0 / speed_ratio

        # Use ffmpeg to adjust speed and output to the desired duration
        (
            ffmpeg
            .input(input_file)
            .filter('atempo', speed_factor)
            .output(output_file)
            .run(overwrite_output=True)
        )

        print(f"Audio adjusted and saved to {output_file} with target duration {target_duration_seconds} seconds")
    except ffmpeg.Error as e:
        print(e.stderr)

def sync_audio():

    translated_json  = open("../ai/translated_json.json")
    translated_chunks = json.load(translated_json)

    combined = AudioSegment.empty()

    for k in range(len(translated_chunks)):
            # Example usage:
        input_file = f"../ai/output_audio/translated_chunk{k}.wav"
        output_file = f"../ai/output_audio/sync_chunk{k}.wav"
        target_duration = translated_chunks[k]["duration"]  # Target duration in seconds
        # print(target_duration)

        adjust_audio_duration(input_file, output_file, target_duration)

        

        # sync_audio(input_file,output_file,target_duration)
        combined+=AudioSegment.from_file(output_file)

    combined.export('../ai/output_audio/full_translated.wav',format='wav')
    print('saved translation')
