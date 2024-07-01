import demucs.separate

audio_file = "../sample_videos/sample1.webm"

# Separate the audio clip into vocals and no vocals
demucs.separate.main(["--mp3", "--two-stems", "vocals", "-n", "mdx_extra", audio_file])