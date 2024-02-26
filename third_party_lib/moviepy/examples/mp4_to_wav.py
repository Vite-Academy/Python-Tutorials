from moviepy.editor import VideoFileClip

# Define input and output filenames
input_file = "video.mp4"
output_file = "video_audio.wav"

# Read the MP4 file
clip = VideoFileClip(input_file)

# Extract the audio stream and write it to a WAV file
clip.audio.write_audiofile(output_file, bitrate="320k")

print("Audio extracted from MP4 and saved as WAV!")
