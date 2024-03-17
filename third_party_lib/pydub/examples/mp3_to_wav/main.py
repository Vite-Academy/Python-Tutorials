from pydub import AudioSegment

# Replace with your file paths
# mp3_file = "never-gonna-give-you-up.mp3"
# wav_file = "never-gonna-give-you-up.wav"

# mp3_file = "fikrlar.mp3"
# wav_file = "fikrlar.wav"

mp3_file = "fikrlar.mp3"
wav_file = "fikrlar.wav"

# Read MP3 and export as WAV
audio = AudioSegment.from_mp3(mp3_file)
audio.export(wav_file, format="wav")

print("Converted MP3 to WAV successfully!")