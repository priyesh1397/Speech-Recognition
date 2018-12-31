import pyttsx3

def speakk(text):
  engine = pyttsx3.init()
  engine.say('Yor are searching in google for : '+text);
  engine.setProperty('volume',0.9)
  engine.runAndWait()