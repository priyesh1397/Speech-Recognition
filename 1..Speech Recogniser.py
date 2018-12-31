import speech_recognition as sr
r=sr.Recognizer()

with sr.Microphone() as source:
    print("Say something : ")
    audio=r.listen(source)

try:
    print("Google just heard : " + r.recognize_google(audio))

except:
    print("There is some pproblem....!!!")