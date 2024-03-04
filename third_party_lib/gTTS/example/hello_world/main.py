# Working with CLI
# gtts-cli --all
# gtts-cli 'Hello world!' --output hello_world.mp3
# gtts-cli "c'est la vie" --lang fr --output cestlavie.mp3
# gtts-cli '你好' --tld .com.hk --lang zh-CN --output 你好.mp3
# gtts-cli 'slow' --slow --output slow.mp3
# gtts-cli 'hello_world'


from gtts import gTTS
tts = gTTS('Hello world!')
tts.save('hello_world.mp3')