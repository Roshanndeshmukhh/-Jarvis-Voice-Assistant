import speech_recognition as sr
import webbrowser
import pyttsx3

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Music library
music = {
    "dooriyan": "https://youtu.be/7z3YeFqd7xQ?si=azxrvfhX2K9QAr0G",
    "a wall of steel": "https://youtu.be/VkKQsmH8kiE?si=jOUex4hrlrKkYd1V",
    "spartan law": "https://youtu.be/eGtF-zkeo9s?si=AJZHBLZb5Ea4Se-J",
}

# Function to make the engine speak the given text
def speak(text):
    engine.say(text)
    engine.runAndWait()


def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower ():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):

        # Extract the song name 
        song = c.lower().replace("play", "").strip()
        print(f"Song requested: {song}")  # Debugging
        if song in music:
            link = music[song]
            webbrowser.open(link)
            speak(f"Playing {song}.")
        else:
            speak(f"Sorry, I couldn't find the song '{song}' in the library.")
    else:
        speak("I didn't understand the command.")
     
if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # listen for the wake word "Jarvis"
        # Obtain audio from the microphone
        r = sr.Recognizer()

        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("yeahh")
                # Listen for command
            with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    
                    processcommand(command)

        except Exception as e:
            print("Error: {0}".format(e))
