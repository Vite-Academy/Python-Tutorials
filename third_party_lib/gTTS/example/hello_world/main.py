# Working with CLI
# gtts-cli 'Hello world!' --output hello_world.mp3

from gtts import gTTS
tts = gTTS('Hello world!')
tts.save('hello_world.mp3')