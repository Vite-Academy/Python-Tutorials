import wave

wav_file = ""

with wave.open(wav_file, "rb") as wav_file:

# Get information about the WAV file
  print(f"Number of channels: {wav_file.getnchannels()}")
  print(f"Sample width: {wav_file.getsampwidth()}")
  print(f"Sampling rate: {wav_file.getframerate()}")
  print(f"Number of frames: {wav_file.getnframes()}")

  # Read all frames at once
  frames = wav_file.readframes(wav_file.getnframes())

  # Do something with the frames data, for example, convert it to numpy array
  # ...
  

