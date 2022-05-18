#hello 
import speech_recognition as sr
r = sr.Recognizer()
audio_source=int(input("which source do you prefer ? \n Enter 1 if your choice is file \n Enter 2 if your choice is microphone \n "))
if(audio_source==1):
        filename=input("enter your file name")
        with sr.AudioFile(filename) as source:
        	audio=r.record(source)
elif(audio_source==2):
    with sr.Microphone() as source:
    	print("Speak Anything :")
    	audio = r.record(source)
try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
except:
	print("Sorry could not recognize what you said")
