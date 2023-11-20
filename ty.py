import speech_recognition 
import filecmp
import gtts 
from playsound import playsound 
from gtts import gTTS 
import pyttsx3 



sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5

def listen_command():
    try:
         with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic,duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio,language='ru-RU').lower()

            text_val = query
            language = 'ru'
            obj = gTTS(text=text_val, lang=language, slow=False)
            obj.save("exam.mp3")


            return query
    except speech_recognition.UnknownValueError:
        return 'Команда не распознана'

def greeting():
    
    engine = pyttsx3.init()
    text = "Здравствуй друг" 
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[0].id)
    engine.say(text) 
    engine.runAndWait() 
    return "Здравствуй Друг"

def zapis():

    engine = pyttsx3.init() 
    text = "Что хотите добавить в список дел?" 
    engine.say(text) 
    engine.runAndWait() 
    print("Что бы вы хотели добавить в список дел")
    

    query = listen_command()

    with open('spisok.txt','a') as file:
        file.write(f'{query}\n')
        engine = pyttsx3.init() 
        text = "Задача " + query + " добавлена в список дел" 
        engine.say(text) 
        engine.runAndWait() 
        return "Задача " + query + " добавлена в список дел "

def main ():
    query = listen_command()
    if query == "привет":
        print(greeting())
    elif query == "добавить задачу":
        print(zapis())

if __name__ == '__main__':
    main()



