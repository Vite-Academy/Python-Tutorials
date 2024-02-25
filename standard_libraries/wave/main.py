import wave

def read_and_write_wav(input_filename, output_filename):
    """Reads data from an input WAV file and writes it to a new WAV file.

    Args:
        input_filename (str): Path to the input WAV file.
        output_filename (str): Path to the output WAV file.

    Raises:
        ValueError: If the input file is not a valid WAV file.
        IOError: If there is an error reading or writing the files.
    """

    try:
        # Open the input file in read binary mode
        with wave.open(input_filename, 'rb') as wav_in:
            # Get the wave parameters
            num_channels = wav_in.getnchannels()
            sampwidth = wav_in.getsampwidth()
            framerate = wav_in.getframerate()
            nframes = wav_in.getnframes()

            # Check if the input file is a valid WAV file
            if wav_in.getcomptype() != 'NONE':
                raise ValueError("Input WAV file must be uncompressed (PCM).")

            # Read the entire audio data in bytes
            audio_data = wav_in.readframes(nframes)

        # Open the output file in write binary mode
        with wave.open(output_filename, 'wb') as wav_out:
            # Set the same wave parameters as the input file
            wav_out.setnchannels(num_channels)
            wav_out.setsampwidth(sampwidth)
            wav_out.setframerate(framerate)
            wav_out.setnframes(nframes)

            # Write the audio data (bytes) to the output file
            wav_out.writeframes(audio_data)

        print(f"Successfully read WAV data from '{input_filename}' and wrote it to '{output_filename}'.")

    except (ValueError, IOError) as e:
        print(f"Error: {e}")

# Example usage
input_filename = 'audio.wav'
output_filename = 'new_audio.wav'
read_and_write_wav(input_filename, output_filename)
