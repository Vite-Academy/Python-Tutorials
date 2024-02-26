import pyaudio
import wave

def play_audio_file(file_path):
    chunk = 1024

    # Open the audio file using 'with' statement
    with wave.open(file_path, 'rb') as wf:
        # Instantiate PyAudio
        p = pyaudio.PyAudio()

        # Open PyAudio stream
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        # Read data
        data = wf.readframes(chunk)

        # Play audio
        while data:
            stream.write(data)
            data = wf.readframes(chunk)

        # Stop and close the stream
        stream.stop_stream()
        stream.close()

        # Terminate PyAudio
        p.terminate()

# Example usage
file_path = 'audio.wav'
play_audio_file(file_path)
