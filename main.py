import speech_recognition as sr
import webbrowser
import pyttsx3
import music_library
import requests
import google.generativeai as genai
import datetime

recognizer = sr.Recognizer()
engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[2].id)  # Change index for a different voice
# engine.setProperty('rate', 175)  # Speed of voice

newsapi = "563e31991c3d45da9efa111aed15e1c1"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    genai.configure(api_key="AIzaSyCxGm_EFvP3GCPs2xS6E806ck2G_RHB_uw")
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(command)
    
    return response.text


# This is capable of opening music, link
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
        

    elif  "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {current_date}")
    
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = music_library.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        # Below 5 line of code is from chatgpt
        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])
            # Print headlines
            for article in articles:
                speak(article["title"])
    
    else:
        output = aiProcess(c)
        speak(output)
        pass

    # print(c)

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        r = sr.Recognizer()

        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening..")
                # audio = r.listen(source, timeout = 2, phrase_time_limit=1)
                audio = r.listen(source, timeout = 5, phrase_time_limit=5)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Yes sir")

                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)

        # except sr.UnknownValueError:
        #     speak("Sorry I couldn't get that")
            
        except Exception as e:
            print("Error; {0}".format(e))
                

