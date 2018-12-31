import pyttsx3

engine=pyttsx3.init()

rate=engine.getProperty('rate')
engine.setProperty('rate',rate+50)
engine.say('Hello,This is Priyesh Ranjan '
               '.I am from Bhagalpur College '
               'of Engineering.I am a final yr student '
               'insiring to leran more in my life '
               'to get much more high position in my carrier...')

engine.runAndWait()