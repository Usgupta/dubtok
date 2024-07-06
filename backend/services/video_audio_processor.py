import subprocess
import moviepy.editor as mpe

def separate_audio_video(input_video, output_audio, output_video):
    # Command to extract audio
    extract_audio_cmd = [
        'ffmpeg',
        '-i', input_video,
        '-q:a', '0',
        '-map', 'a',
        output_audio,
        "-y"
    ]
    
    # Command to extract video without audio
    extract_video_cmd = [
        'ffmpeg',
        '-i', input_video,
        '-an',
        '-vcodec', 'copy',
        output_video,
        "-y"
    ]
    
    # Run the command to extract audio
    subprocess.run(extract_audio_cmd, check=True)
    print(f"Audio extracted to {output_audio}")
    
    # Run the command to extract video without audio
    subprocess.run(extract_video_cmd, check=True)
    print(f"Video extracted to {output_video}")


def combine_audio_video(input_video, input_audio, output_video):
    video_clip = mpe.VideoFileClip(input_video)
    audio_clip = mpe.AudioFileClip(input_audio)
    final_audio = mpe.CompositeAudioClip([audio_clip])
    final_clip = video_clip.set_audio(final_audio)
    final_clip.write_videofile(output_video, codec="libx264", audio_codec="aac")
    
