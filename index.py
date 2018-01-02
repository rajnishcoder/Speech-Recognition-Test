import speech_recognition as sr
 
# Record Audio
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
 
# Speech recognition using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    # to changhe language use r.recognize_google(audio, language="in") 
    output = r.recognize_google(audio)
    print(output)
except sr.UnknownValueError:
    print("Sorry I did not understand! Can you say it again?")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))