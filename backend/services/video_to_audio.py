import subprocess

def separate_audio_video(input_video, output_audio, output_video):
    # Command to extract audio
    extract_audio_cmd = [
        'ffmpeg',
        '-i', input_video,
        '-q:a', '0',
        '-map', 'a',
        output_audio
    ]
    
    # Command to extract video without audio
    extract_video_cmd = [
        'ffmpeg',
        '-i', input_video,
        '-an',
        '-vcodec', 'copy',
        output_video
    ]
    
    # Run the command to extract audio
    subprocess.run(extract_audio_cmd, check=True)
    print(f"Audio extracted to {output_audio}")
    
    # Run the command to extract video without audio
    subprocess.run(extract_video_cmd, check=True)
    print(f"Video extracted to {output_video}")
