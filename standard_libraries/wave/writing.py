import wave
import numpy as np

# Define parameters
sample_rate = 44100
frequency = 440

# Generate sine wave data
duration = 1  # seconds
time = np.linspace(0, duration, int(duration * sample_rate))
data = np.sin(2 * np.pi * frequency * time)

# Create WAV file
with wave.open("output.wav", "wb") as wav_file:
  wav_file.setparams((1, 2, sample_rate, len(data), "NONE", "not compressed"))
  wav_file.writeframes(data.astype(np.int16).tobytes())

