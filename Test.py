from playsound import playsound
import os
from gtts import gTTS
import JarvisCode

#Use this file to create new permant audio files
file_path = "example.mp3"
text = "Input text here"

speech = gTTS(text=text, lang=JarvisCode.lang, slow=False,
              tld=JarvisCode.tld)
speech.save(file_path)
playsound(file_path)

