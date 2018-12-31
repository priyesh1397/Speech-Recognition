import pyttsx3

voices=engine=pyttsx3.init()

engine.getProperty('voices')
    # FOR COMMON
for voice in voices:
   engine.setProperty('voice', voice.id)
   print(voice.id)
   engine.say('Hello,This is Priyesh Ranjan '
              '.I am from Bhagalpur College '
              'of Engineering.I am a final yr student '
              'insiring to leran more in my life '
              'to get much more high position in my carrier...')


   #  FOR FEMALE VOICE
engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft'
                       '\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
engine.say('Hello,This is Priyesh Ranjan '
               '.I am from Bhagalpur College '
               'of Engineering.I am a final yr student '
               'insiring to leran more in my life '
               'to get much more high position in my carrier...')

   #   FOR MALE VOICE

engine.setProperty('voice','HKEY_LOCAL_MACHINE'
                           '\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0')
engine.say('Hello,This is Priyesh Ranjan '
               '.I am from Bhagalpur College '
               'of Engineering.I am a final yr student '
               'insiring to leran more in my life '
               'to get much more high position in my carrier...')
engine.runAndWait()