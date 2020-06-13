import tkinter as tk
from googletrans import Translator

win = tk.Tk()

win.title("Translator")
win.geometry("300x100")


def translator():
    lang = entry.get()
    word = entry1.get()
    translator = Translator(service_urls=["translate.google.com"])
    translation = translator.translate(word, dest=f'{lang}')
    label1 = tk.Label(win, text=f'Translated word  = {translation.text}', bg="#FF3E96")
    label1.grid(row=4, column=0, columnspan=5)


def src():
    lang = entry.get()
    word = entry1.get()
    translator = Translator(service_urls=["translate.google.com"])
    translation = translator.translate(word, dest=f'{lang}')
    label2 = tk.Label(win, text=f'Source Language = {translation.src}')
    label2.grid(row=4, column=0, columnspan=5)


def pron():
    lang = entry.get()
    word = entry1.get()
    translator = Translator(service_urls=["translate.google.com"])
    translation = translator.translate(word, dest=f'{lang}')
    label2 = tk.Label(win, text=f'Pronunciation = {translation.pronunciation}')
    label2.grid(row=4, column=0, columnspan=5)


label = tk.Label(win, text="Language : ")
label.grid(row=0, column=0)

entry = tk.Entry(win)
entry.grid(row=0, column=1)

label1 = tk.Label(win, text="Write Here : ")
label1.grid(row=1, column=0)

entry1 = tk.Entry(win)
entry1.grid(row=1, column=1)

button = tk.Button(win, text="Translate", command=translator)
button.grid(row=2, column=0)

button1 = tk.Button(win, text="Source Lang.", command=src)
button1.grid(row=2, column=1)

button2 = tk.Button(win, text="Pronunciation", command=pron)
button2.grid(row=2, column=2)

win.mainloop()
