# Example same code
# https://github.com/alphacep/vosk-api/blob/master/python/example/test_simple.py
# https://github.com/alphacep/vosk-api/blob/master/python/example/test_ep.py

import sys
import os
import wave
import json
from vosk import Model, KaldiRecognizer, SetLogLevel, list_models, list_languages, open_dll

# You can set log level to -1 to disable debug messages
SetLogLevel(0)

# print(list_models()) # List models
# print(list_languages()) # List anguages
# print(open_dll()) # Check sys platform


def stt(wav_file):
    wf = wave.open(wav_file, "rb")
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
        print("Audio file must be WAV format mono PCM.")
        sys.exit(1)

    # Open the wave file
    with wave.open(wav_file, "rb") as wf:
        # Load the Vosk model 
        model = Model(r"./vosk-model-small-uz-0.22")
        # Create a KaldiRecognizer
        rec = KaldiRecognizer(model, wf.getframerate())


        while True:
            data = wf.readframes(wf.getnframes())  # Process audio in chunks

            if len(data) == 0:
                break

            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                return result["text"]
            else:
                # Handle partial results if needed
                pass

wav_file = "/Users/shakhzodtojiev/Downloads/Coding/Python-Tutorials/media/temp.wav"
result_text = stt(wav_file)
print("Recognized text:", result_text)
