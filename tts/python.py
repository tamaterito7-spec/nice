#Convert Speech to text and text to Speech: PythonGeeks
#import packages
from tkinter import ttk
from gtts import gTTS, lang
import os
from tkinter import * 
from tkinter import messagebox
import speech_recognition as r

#define functions
#text to speech conversion
def text_to_speech():
    text = text_entry.get("1.0", "end-1c").strip()
    selected_lang = accent_combo.get()

    if len(text) <= 1:
        messagebox.showerror("Error", "Please enter some text.")
        return
    if not selected_lang:
        messagebox.showerror("Error", "Please select a language.")
        return

    lang_code = LANGUAGE_MAP.get(selected_lang)
    if not lang_code:
        messagebox.showerror("Error", "Invalid language.")
        return

    try:
        speech = gTTS(text=text, lang=lang_code, slow=False)
        speech.save("text.mp3")
        os.system("mpg123 text.mp3")
    except Exception as e:
        messagebox.showerror("Error", f"TTS failed: {e}")
def list_languages():
    #access languages and access codes using lang.tts_lands()
    messagebox.showinfo(message=list(lang.tts_langs().items()))
#Python speech to text conversion
def speech_to_text():

    recorder = sr.Recognizer()
    try:
        duration =int(duration_entry.get())
    except:
        messagebox.showerror(message="Enter the duration")
        return
    #use the microphone
    messagebox.showinfo(message="Speak into the microphone and wait after finishing the recording")
    with sr.Microphone() as mic:
        #Prompt the user to record
        #Record audio from the user
        recorder.adjust_for_ambient_noise(mic)
        audio_input = recorder.listen(mic, duration=duration)
        try:
            text_output =recorder.recognize_google(audio_input)
            #Display the output
            messagebox.showinfo(message="You said:\n" + text_output)
        except:
            messagebox.showerror(message="Couldn't process audio input.")
#Invoke a call to class to view a window
window = Tk()
#Set dimensions of window and title
window.geometry("500x300")
window.title("Convert Speech to text and text to Speech: PythonGeeks")
title_label = Label(window, text="Convert Speech to text and text to Speech:PythonGeeks").pack()

#Read inputs
#text_to_speech input
text_label = Label(window, text="Text:").place(x=10,y=20)
text_entry = Text(window, width=30,height=5)
text_entry.place(x=80,y=20)

#Accent input
accent_label = Label(window, text="Accent:").place(x=10, y=130)

# Language mapping: User-friendly name → gTTS code
LANGUAGE_MAP = {
    "English": "en",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Italian": "it",
    "Portuguese": "pt",
    "Hindi": "hi",
    "Chinese (Mandarin)": "zh-CN",
    "Japanese": "ja",
    "Korean": "ko",
    "Arabic": "ar",
    "Russian": "ru",
    "Dutch": "nl",
    "Turkish": "tr",
    "Polish": "pl"
}

accent_combo = ttk.Combobox(window, values=list(LANGUAGE_MAP.keys()), state="readonly", width=23)
accent_combo.place(x=81, y=130)
accent_combo.set("English")  # Default selection
duration_label = Label(window, text="Duration:").place(x=10,y=160)
duration_entry = Entry(window, width=26)
duration_entry.place(x=80,y=160)

#Perform the functions
button1 = Button(window,text="List languages", bg =
'Turquoise',fg='Red',command=list_languages).place(x=10,y=190)
button2 = Button(window,text="Convert Text to Speech", bg =
'Turquoise',fg='Red',command=text_to_speech).place(x=130,y=190)
button3 = Button(window,text="Convert Speech to Text", bg =
'Turquoise',fg='Red',command=speech_to_text).place(x=305,y=190)

#close the app
window.mainloop()