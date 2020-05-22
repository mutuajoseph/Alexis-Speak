# import the speech recognition library
import speech_recognition as sr 
from time import ctime
import webbrowser
import time
import random
import os
import playsound
from gtts import gTTS

# create an instance of the recognizer class 
r = sr.Recognizer()

def record_audio(ask = False):
    # specify the audio source
    with sr.Microphone() as source:
        # print('Say something')
        if ask:
            alexis_speak(ask)
        # inside the recognizer class we need to access the listen method
        # this will be used to listen/ capture the audio from the source 
        audio = r.listen(source)
        voice_data = ''
        try:
            # We then need to recognize/recognize the audio captured and convert it to text
            # recognize_google will process the audio
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            # this message will be printed if alexis does not understand what you are saying
            alexis_speak('Sorry, I did not understand what you are said')
        except sr.RequestError:
            alexis_speak('Sorry, My speech service is down')
        return voice_data

def alexis_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'what is your name' in voice_data:
        alexis_speak('My name is alexis')
    if 'what time is it' in voice_data:
        alexis_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        alexis_speak('Here is what i found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp'
        webbrowser.get().open(url)
        alexis_speak('Here is the location of ' + location)
    if 'exit' in voice_data:
        alexis_speak('Goodbye')
        exit()


# To continously listen we will need to use the time property
time.sleep(1)
alexis_speak('How can i help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)


