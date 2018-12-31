import speech_recognition as sr

r=sr.Recognizer()

audio='put the song with title in "wav","aiff","flac"'
with sr.AudioFile(audio) as source:
    print('Say Something : ')
    audio=r.record(source)
    print('Done it....!!!!')

try:
    text=r.recognize_google(audio)
    print(text)

except:
    print('You have to select small file')

