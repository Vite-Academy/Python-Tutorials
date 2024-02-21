from pydub import AudioSegment

# Replace with your file paths
mp3_file = "never-gonna-give-you-up.mp3"
wav_file = "never-gonna-give-you-up.wav"

# Read WAV and export as MP3
audio = AudioSegment.from_wav(wav_file)
audio.export(mp3_file, format="mp3")

print("Converted WAV to MP3 successfully!")