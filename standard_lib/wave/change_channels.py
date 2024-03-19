import wave

def change_channels(input_file, output_file, new_channels):
    with wave.open(input_file, 'rb') as wav_in:
        params = wav_in.getparams()
        # Modify number of channels
        new_params = wave._wave_params(params[0], params[1], params[2], params[3], new_channels, params[5])
        with wave.open(output_file, 'wb') as wav_out:
            wav_out.setparams(new_params)
            data = wav_in.readframes(wav_in.getnframes())
            wav_out.writeframes(data)

# Example usage:
input_file = 'fikrlar.wav'
output_file = 'fikrlar_edited.wav'
new_channels = 1  # Change this to the desired number of channels
change_channels(input_file, output_file, new_channels)
