import wave
import json
from vosk import Model, KaldiRecognizer, list_models, list_languages, open_dll

# print(list_models()) # List models
# print(list_languages()) # List anguages
# print(open_dll()) # Check sys platform


def stt(wav_file):
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
