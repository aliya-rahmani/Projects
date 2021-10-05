import speech_recognition as sr
from gtts import gTTS
import os
voice = ""
while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio = r.listen(source)
            text = r.recognize_google(audio)
            print(text)
            if text=='stop':
                break
            text = r.recognize_google(audio)
            voice = voice+str(text)
        except:
            print("Say something......")
hr = gTTS(text=voice, slow=False)
hr.save("1.wav") #this will save this file in you users folder and change every time you run it if you don't change the name
