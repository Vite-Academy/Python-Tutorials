import wave

# video_audio.wav
wav_file = "audio.wav"

with wave.open(wav_file, "rb") as wav_file:

# getnchannels() -> Returns number of audio channels (1 for mono, 2 for stereo).
  print(f"Number of channels: {wav_file.getnchannels()}")

# getsampwidth() -> Returns sample width in bytes. (e.g., 2 for 16-bit)
  print(f"Sample width: {wav_file.getsampwidth()}")

# getframerate() -> Returns sampling frequency. Hz (e.g., 44100 = 44.1 kHz)
  print(f"Sampling rate: {wav_file.getframerate()}")

# getnframes() -> Returns number of audio frames in the file.
  print(f"Number of frames: {wav_file.getnframes()}")
  
# getcomptype() -> Returns compression type ('NONE' is the only supported type).
  print(f"Compression type: {wav_file.getnframes()}")

