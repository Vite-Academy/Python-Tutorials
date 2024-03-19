from pydub import AudioSegment

def convert_mp4_to_wav(mp4_file, wav_file):
    # Load the MP4 file
    audio = AudioSegment.from_file(mp4_file, format="mp4")

    # Export the audio to WAV format
    audio.export(wav_file, format="wav", parameters=["-ac", "1"])

# Specify the paths of the input MP4 file and the output WAV file
input_mp4_file = "nutq.mp4"
output_wav_file = "nutq.wav"

# Convert MP4 to WAV
convert_mp4_to_wav(input_mp4_file, output_wav_file)
