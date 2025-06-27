import speech_recognition as sr
import os
import webbrowser

def say(text):
    os.system(f'espeak "{text}"')

def takecammand():
    r = sr.Recognizer() # Recognizer() is a class from the speech_recognition library. It creates an object (r) that: 1.Can listen to audio 2.Can understand and convert speech into text
    with sr.Microphone() as source: #opens your default microphone for listening.
        r.pause_threshold = 1 #: If the user stops speaking for more than 1 second, it assumes you're done.
        audio = r.listen(source) #This records the audio using the microphone.
        try :
            query = r.recognize_google(audio, language='en-in') #This sends the audio to Google's Speech Recognition API to converts the spoken voice into text.
            print(f'user said: {query}')
            return query
        except Exception as e:
            return " sorry some erroe occurred"
if __name__ == '__main__':
    print('PyCharm')
    say("hii am Nova A.I. How can I help you")
    while True:
     print("listnning....")
     query = takecammand()
     sites = [["youtube","https://youtube.com"],
             ["chatgpt","https://chatgpt.com"],
             ["whatsapp","https://whatsapp.com"],]
     for site in sites:
        if f"open {site[0]}".lower() in query.lower():
            say(f"open site {site[0]} sir...")
            webbrowser.open(site[1])
     #say(text)