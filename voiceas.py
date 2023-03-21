#what is breathing status
#where is the bulk of injury situated
#please check for any lacerations
#please check if there are any fracture 

    

import pyttsx3
import speech_recognition as sr
import os



engi = pyttsx3.init()
voi = engi.getProperty("voices")
engi.setProperty('voice', voi[1].id)

def speak(audio):
    engi.say(audio)
    print(audio)
    engi.runAndWait()

def talk():
    input=sr.Recognizer()
    with sr.Microphone() as source:
        audio=input.listen(source)
        data=""
        try:
            data=input.recognize_google(audio)
            print("Your question is, " + data)
            
        except sr.UnknownValueError:
            print("Sorry I did not hear your question, Please repeat again.")
    return data
def readinput(prompt):
    otp=prompt.split()
    return otp

def strttalk(val):
    if val==1:
        speak("hello there, Eir at your service, whats the emergency")
    elif val == 2:
        speak("is the victim consious and breadthing")
    elif val == 3:
         speak("is the victim in need of cpr if not check for laciration and bleading")
    elif val== 4:
         speak("check for laciration and bleading")
    elif val == 5:
         speak("where is the bulk of injury located")


if __name__ == '__main__':
    clear = lambda: os.system('cls')
    val=1
    while True:
        strttalk(val)

        prompt=talk().lower()


       
        if any(map(lambda w: w in prompt, ('accident','crash','injury'))):
                filel= open(r'accidentbase.txt',"r")
                speakingLines=filel.read()
                speak(speakingLines)
                val=2

        elif 'exit' in prompt:
            speak("Thanks for giving me your time")
            exit() 
        
        elif any(map(lambda w: w in prompt, ('breath','not breathing','trouble breathing'))):
                filel= open(r'breadth.txt',"r")
                speakingLines=filel.read()
                speak(speakingLines)
                val=3
        
        elif any(map(lambda w: w in prompt, ('cpr','chest compression','Cardiopulmonary','resuscitation'))):
                filel= open(r'cpr.txt',"r")
                speakingLines=filel.read()
                speak(speakingLines)       
                val=4 