import librosa
import soundfile as sf

def convert_to_standard_wav(input_file, output_file):
    try:
        # Read the problematic audio file
        data, sample_rate = librosa.load(input_file, sr=None)
        
        # Write the data to a new WAV file
        sf.write(output_file, data, sample_rate)
    except Exception as e:
        print(f"Error: {e}")

# Example usage
input_file = '/Users/shakhzodtojiev/Downloads/Coding/Python-Tutorials/media/recording.wav'  # Change this to the path of your problematic audio file
output_file = 'standard_file.wav'     # Path for the output standard WAV file
convert_to_standard_wav(input_file, output_file)
