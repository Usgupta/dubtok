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
    # Load video and audio clips
    video_clip = mpe.VideoFileClip(input_video,fps_source="fps")
    audio_clip = mpe.AudioFileClip(input_audio)
    
    # Set the duration of the audio to match the video duration
    if audio_clip.duration < video_clip.duration:
        silence_duration = video_clip.duration - audio_clip.duration
        silence = mpe.AudioClip(lambda t: [0], duration=silence_duration)
        audio_clip = mpe.concatenate_audioclips([audio_clip, silence])
        
    # Create a composite audio clip
    final_audio = mpe.CompositeAudioClip([audio_clip])

    # Set the final audio to the video clip
    final_clip = video_clip.set_audio(final_audio)
    
    # Write the final video to a file
    final_clip.write_videofile(output_video, codec="libx264", audio_codec="aac")
    # final_audio.set_fps(44100).write_audiofile("audio.mp3",codec='aac')

# input_video='../../uploads/cx_noaudio.mp4'
# input_audio='../../ai/output_audio/full_translated.wav'
# output_video='combine.mp4'
    
# combine_audio_video(input_video,input_audio,output_video)