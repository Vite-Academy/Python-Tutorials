from pydub import AudioSegment

def convert_to_pcm(input_file, output_file):
    sound = AudioSegment.from_file(input_file)
    sound.export(output_file, format="wav", parameters=["-ac", "1"])  # Export as uncompressed PCM (mono)

# Example usage:
# input_file = 'fikrlar.wav'
# output_file = 'fikrlar_pcm.wav'

input_file = 'yoshlar.wav'
output_file = 'yoshlar_pcm.wav'

convert_to_pcm(input_file, output_file)
