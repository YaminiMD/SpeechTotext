#speech to text
import speech_recognition as s
r=s.Recognizer()
print(s.Microphone.list_microphone_names())
with s.Microphone() as src:
    audio=r.listen(src)
print(r.recognize_google(audio))


'''#speetch to text
import speech_recognition as s
import wikipedia
import pyttsx3

r=s.Recognizer()

engine=pyttsx3.init()

with s.Microphone() as src:
    r.adjust_for_ambient_noise(src)
    audio=r.listen(src)

text=r.recognize_google(audio)
print(text)

if "what is" in text:
    a=wikipedia.summary(text[7:])
    engine.say(a)
    engine.runAndWait()'''
