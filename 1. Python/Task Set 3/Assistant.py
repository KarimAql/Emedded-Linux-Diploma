import webbrowser
from time import ctime
import os
import vlc
from gtts import gTTS
import random
import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Create VLC instance
vlc_instance = vlc.Instance()

# Create a media player instance
player = vlc_instance.media_player_new()

def Bixby_Speak(audios):
    tts = gTTS(text=audios, lang='en', slow=False)
    audioF = 'audio.mp3'
    tts.save(audioF)
    
    # Load the audio file
    media = vlc_instance.media_new(audioF)

    # Set the media to the player
    player.set_media(media)

    # Start playing the audio
    player.play()

    # Wait for playback to finish
    while player.is_playing():
        continue
    
    os.remove(audioF)

def record(ask=False):
    with sr.Microphone(device_index=None) as source:
        r.adjust_for_ambient_noise(source)
        if ask:
            Bixby_Speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio, language="en")
        except sr.UnknownValueError:
            Bixby_Speak("sorry, i did not get that")
        except sr.RequestError:
            Bixby_Speak("sorry, Service is Down")
        return voice_data.lower()


def Respond(voice_data):
    if 'name' in voice_data or 'my name' in voice_data:
        Bixby_Speak('Hello, Karim')
    if 'Time' in voice_data:
        Bixby_Speak(ctime())
    if 'search' in voice_data or 'google' in voice_data:
        search = record('what dow want to search')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        Bixby_Speak('Here is what i Found For' + search)

    if 'where' in voice_data or 'location' in voice_data:
        location = record("what location do you want me to seach for")
        url = 'https://google.nl/maps/place/' + location + '/&amp'
        webbrowser.get().open(url)
        Bixby_Speak('Here is what i Found For' + location)
        
    if 'exit' in voice_data:
        exit()
 

Bixby_Speak('How Can I help You')
while 1:
    voice_data = record()
    Respond(voice_data)
