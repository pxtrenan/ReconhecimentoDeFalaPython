import speech_recognition as sr
import tkinter as tk

def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        status_label.config(text="Diga alguma coisa!")
        status_label.update()
        audio = r.listen(source)
    
    try:
        result_label.config(text="Você disse: " + r.recognize_google(audio, language='pt-BR'))
    except sr.UnknownValueError:
        result_label.config(text="Não foi possível entender o que você disse")
    except sr.RequestError as e:
        result_label.config(text="Não foi possível estabelecer uma conexão com o serviço de reconhecimento de fala; {0}".format(e))
    
    result_label.update()


window = tk.Tk()
window.title("Reconhecimento de Voz")


status_label = tk.Label(window, text="")
result_label = tk.Label(window, text="")
button = tk.Button(window, text="Reconhecer Fala", command=recognize_speech)


status_label.pack()
result_label.pack()
button.pack()


window.mainloop()