from playsound import playsound
import os
from gtts import gTTS
import JarvisCode

# Use this file to create new permant audio files
# If you would like to create a personalized start up message you can replace the currant welcome file
file_path = "Welcome.mp3"
text = "Input text here"

speech = gTTS(text=text, lang=JarvisCode.lang, slow=False,
              tld=JarvisCode.tld)
speech.save(file_path)
playsound(file_path)

