import speech_recognition as sr
import webbrowser
import pyaudio

if __name__ == "__main__":
    # Waiting for you to say "This is so sad, Alexa play Despacito"
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say This is so sad. Alexa play Despacito")
        audio = r.listen(source)

    try:
        speech = r.recognize_sphinx(audio)
        if "sad" in speech and ("alexa" in speech or "Alexa" in speech) and "play" in speech:
           webbrowser.open("https://soundcloud.com/luisfonsiofficial/despacito", new=2)
    except sr.UnknownValueError:
        print("You did not say This is so sad, Alexa play Despacito")
    except sr.RequestError as e:
        print("Despacito error; {0}".format(e))
