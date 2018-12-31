import speech_recognition as sr

r=sr.Recognizer()

with sr.Microphone() as source:
    print('Say Something....!!!!')
    audio=r.listen(source)
    print('Done it...!!!')

try:
    print('You just spoke in hindi as : ')
    text=r.recognize_google(audio,language='hi-IN')
    print(text)
    print(r.recognize_google(audio))

except:
    print("you are going something wrong....")


