import os
import time
# pip install pyaudio
import pyaudio
# pip install playsound==1.2.2
from playsound import playsound
# pip install gTTS
from gtts import gTTS
# pip install openai
import openai
# pip install SpeechRecognition
import speech_recognition as sr

import MyAPIKey

lang = 'en'
# Accent
tld = 'ie'
#Linking to my API key
openai.api_key = MyAPIKey.key
stopKey = ""


audio_file = os.path.dirname(__file__) + '\Welcome.mp3'
playsound(audio_file)
file_name = " response.mp3"

while True:
    def get_audio():
        r = sr.Recognizer()
        with sr.Microphone(device_index=1) as source:
            audio = r.listen(source)
            said = ""

            try:
                said = r.recognize_google(audio)
                print(said)
                global stopKey
                stopKey = said

                if "Friday" in said:
                    try:
                        os.remove(file_name)
                    except Exception:
                        print("no current file")
                    new_string = said.replace("Friday ", "")
                    new_string = new_string.strip()
                    print(new_string)
                    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                                              messages=[{"role": "user", "content": new_string}],
                                                              temperature=0)
                    text = completion.choices[0].message["content"]
                    speech = gTTS(text=text, lang=lang, slow=False, tld=tld)
                    speech.save(file_name)
                    print(text)
                    playsound(file_name)
            except Exception as error:
                print(error)

        return said

    if "stop" in stopKey:
        break

    get_audio()

