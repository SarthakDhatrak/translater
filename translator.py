from tkinter import *
from tkinter import ttk, messagebox
from textblob import TextBlob
from googletrans import LANGUAGES

root = Tk()
root.title("Google Translator")
root.geometry("1080x400")


def label_change():
    c = combo1.get()
    c1 = combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000, label_change)


def translate_now():
    try:
        text_ = text1.get(1.0, END).strip()
        c2 = combo1.get()
        c3 = combo2.get()
        if text_:
            words = TextBlob(text_)
            lan = words.detect_language()
            print(f"Detected language: {lan}")  # Debugging

            # Find the language code for the target language
            for code, lang in language.items():
                if lang == c3:
                    lan_ = code
                    break

            print(f"Translating from {lan} to {lan_}")  # Debugging
            translated_words = words.translate(from_lang=lan, to=lan_)
            print(f"Translated text: {translated_words}")  # Debugging

            text2.delete(1.0, END)
            text2.insert(END, translated_words)
    except Exception as e:
        messagebox.showerror("Googletrans", f"Error: {str(e)}")


# Load icon and images
image_icon = PhotoImage(file="google.png")
root.iconphoto(False, image_icon)

arrow_image = PhotoImage(file="arrow.png")
image_label = Label(root, image=arrow_image, width=150)
image_label.place(x=460, y=50)

# Language dictionary
language = LANGUAGES
languageV = list(language.values())

# ComboBox for source language
combo1 = ttk.Combobox(root, values=languageV, font=("Roboto 14"), state="r")
combo1.place(x=110, y=20)
combo1.set("ENGLISH")

label1 = Label(root, text="English", font=("segoe 30 bold"), bg="white", width=18, bd=5, relief=GROOVE)
label1.place(x=10, y=50)

f = Frame(root, bg="black", bd=5)
f.place(x=10, y=118, width=440, height=210)

text1 = Text(f, font="Robote 20", bg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, height=200, width=430)

scrollbar1 = Scrollbar(f)
scrollbar1.pack(side=RIGHT, fill=Y)
scrollbar1.config(command=text1.yview)
text1.config(yscrollcommand=scrollbar1.set)

# ComboBox for target language
combo2 = ttk.Combobox(root, values=languageV, font=("Roboto 14"), state="r")
combo2.place(x=730, y=20)
combo2.set("SELECT LANGUAGE")

label2 = Label(root, text="English", font=("segoe 30 bold"), bg="white", width=18, bd=5, relief=GROOVE)
label2.place(x=620, y=50)

f1 = Frame(root, bg="black", bd=5)
f1.place(x=620, y=118, width=440, height=210)

text2 = Text(f1, font="Robote 20", bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, height=200, width=430)

scrollbar2 = Scrollbar(f1)
scrollbar2.pack(side=RIGHT, fill=Y)
scrollbar2.config(command=text2.yview)
text2.config(yscrollcommand=scrollbar2.set)

# Translate button
translate = Button(root, text="Translate", font="Roboto 15 bold italic", activebackground="purple", cursor="hand2",
                   bd=5, fg="white", bg="red", command=translate_now)
translate.place(x=480, y=250)

label_change()

root.configure(background="white")
root.mainloop()
