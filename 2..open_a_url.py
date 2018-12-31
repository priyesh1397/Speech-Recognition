                            # MODULES
import speech_recognition as sr
import webbrowser as wb

r=sr.Recognizer()
                            # GOOGLE PATH
google_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
                            # COLLECTING WORDS WHAT WE SPEAK.......
with sr.Microphone() as source:
    print("Please speak to check in google : ")
    audio=r.listen(source)
    print("Done it...lets check your words in google...")
                            # CONVERTING AUDIO TO TEXT AND THEN SEARCH.......
try:
    text= r.recognize_google(audio)
    print("google is going to check " + text)
    wb.get(google_path).open(text)

except Exception as e:
    print(e)