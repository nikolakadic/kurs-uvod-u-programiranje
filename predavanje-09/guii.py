# GUI = graphical user interface
from tkinter import *

from tkinter import messagebox

root = Tk()


label = Label(root, text='Uvod u programiranje')
label2 = Label(root, text='Kurs za pocetnike')

label.grid(row=0,column=0)
# label2.grid(row=3,column=0)
#pack i grid ne mogu da se kombinuju

root.title('Uvod')


def nesto_promijenjeno():
    print('Change')



sadrzaj_polja = StringVar()

entry1 = Entry(root, textvariable=sadrzaj_polja)

entry1.grid(row=6, column=0)

def dugmeKliknuto():
    # messagebox.showerror("Pogrešna akcija", "Hello World")
    label5 = Label(root, text=sadrzaj_polja.get())
    label5.grid(row=7,column=0)

# EVENT (klikovi, pomjeranja ... - akcije koje korisnik sprovodi nad interfejsom)
# EVENTLISTENER
# EVENTHANDLER


button = Button(root, text='Click me', command=dugmeKliknuto)
# button2 = Button(root, text='Click me2', command=dugmeKliknuto)
button.grid(row=1, column=0)
# button2.grid(row=4, column=0)

msg_box = Message(root, text='Zdravo!')
msg_box.grid(row=5,column=0)

root.mainloop()