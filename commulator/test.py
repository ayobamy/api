#!/usr/bin/python3
from gtts import gTTS

text_speech = gTTS(text="Hello guys! Welcome to my blog", lang="en")

text_speech.save('sample.mp3')
