from tkinter import *

from tkinter import messagebox


root = Tk()
root.title('Story telling')


ime = StringVar()
prezime = StringVar()
mjesto_rodjenja = StringVar()
datum_rodjenja = StringVar()


entry_ime = Entry(root, textvariable=ime)
entry_prezime = Entry(root, textvariable=prezime)
entry_mjesto_rodjenja = Entry(root, textvariable=mjesto_rodjenja)
entry_datum_rodjenja = Entry(root, textvariable=datum_rodjenja)

label_ime = Label(root, text='Ime')
label_prezime = Label(root, text='Prezime')
label_mjesto = Label(root, text='Mjesto rodjenja')
label_datum = Label(root, text='Datum rodjenja')


entry_ime.grid(row=1, column=0)
entry_prezime.grid(row=3, column=0)
entry_mjesto_rodjenja.grid(row=5, column=0)
entry_datum_rodjenja.grid(row=7, column=0)

label_ime.grid(row=0, column=0)
label_prezime.grid(row=2, column=0)
label_mjesto.grid(row=4, column=0)
label_datum.grid(row=6, column=0)


def create_story():
    f = open('bazapodataka.txt', 'a')
    zapis = '\n' + ime.get() + prezime.get() + mjesto_rodjenja.get() + datum_rodjenja.get()
    f.writelines(zapis)
    # print('Zdravo, ja sam', ime.get(), prezime.get(), 'rodjen u gradu zvanom', mjesto_rodjenja.get(), ', datuma:', datum_rodjenja.get())

posalji = Button(root, text='Posalji', command=create_story)
posalji.grid(row=8, column=0)

root.mainloop()