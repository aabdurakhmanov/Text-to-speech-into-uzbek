"""
    Bu dastur Text to speech yani Matnni talaffuz qilish dasturi
    dasturning imkoniyatlari:
        - Istalgan matnni talaffuz qilish.
        - txt, doc, docx, exel formatidagi faylarni o`qish.
        - Matnlarni o`zgartirish kiritgan holda yoki o`zgarishsiz saqlash imkoniyati.
        - Talaffuzni 3 uch xil nutqda tinglash mumkun.
        - O`ziga hos dizaynga ega.
        -


"""


import pyttsx3
from tkinter import *
from tkinter import filedialog


# create tkinter Desktop app
root = Tk()
root.title('text_to_speech')
root.geometry('1366x710')
root.iconbitmap('D:\™chromes™/text.ico')
root.resizable(True, True)

bg = PhotoImage(file="images/splash.png")
my_label = Label(root, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)



# Function for speech in text

def talk():
    engine = pyttsx3.init()
    engine.setProperty('rate', 130)

    voices = engine.getProperty('voices')

    engine.setProperty('voice', voices[2].id)
    engine.say(my_entry.get())

    engine.runAndWait()

    my_entry.delete(0,END)



# Function for speech to any text file

def talk_file():
    engine = pyttsx3.init()
    engine.setProperty('rate', 130)

    voices = engine.getProperty('voices')

    engine.setProperty('voice', voices[2].id)
    engine.say(my_text.get("1.0",'end-1c'))

    engine.runAndWait()



# Function for open file

def open_file():
    text_filepath = filedialog.askopenfilename(
        initialdir='E:\Projects/text_tospeech_diplomwork/file/',
        title='Open file',
        filetypes=(("Text Files", "*.txt"),
                   ("All files", "*.*"))
    )
    text_file = open(text_filepath,
                     'r', encoding='ascii',
                     errors='ignore',
                     )
    stuff = text_file.read()

    my_text.insert(END, stuff)
    text_file.close()




# Function for save file

def save_file():
    text_file = filedialog.askopenfilename(
        initialdir='E:\Projects/text_tospeech_diplomwork/file/',
        title='Open file',
        filetypes=(('Text Files', '*.txt'),
                   ('All files', '*.*'))
    )
    text_file = open(text_file, 'w')
    text_file.write(my_text.get(1.0, END))


my_entry = Entry(
                 root,
                 font=('Helvetica', 90)
                 )
my_entry.pack(pady=20)



# button_img = PhotoImage(width=1, height=1)

my_button = Button(
                   root,
                   text='Listen',
                   command=talk,
                   compound='c',
                   font=('Helvetica', 12),
                   )

my_button.pack(pady=10)
my_button.place(
                anchor="nw",
                x=650,
                y=165,
)



# Open file place

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
my_text = Text(
               root,
               width=95,
               height=12,
               bg='silver',
               font=('Impact', 20, 'italic'),
               )
my_text.pack(pady=20)

my_text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=my_text.yview)


# Open text file like txt

open_button = Button(
                     root,
                     text='Open text file',
                     command=open_file,
                     )
open_button.pack(pady=5)
open_button.place(
            x=550,
            y=620,
)



# To talk file text to speech

speech_file_button = Button(
                            root,
                            text='Speech text file',
                            command=talk_file
                            )
speech_file_button.pack(pady=5)
speech_file_button.place(
                         x=650,
                         y=620
)



# File save if file changed

save_button = Button(
                     root,
                     text='Save File',
                     command=save_file
                     )
save_button.pack(pady=5)
save_button.place(
                  x=760,
                  y=620
)


root.mainloop()
