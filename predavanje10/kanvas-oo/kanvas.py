from tkinter import *
from tkinter import filedialog


root = Tk()

root.title('Kanvas')

canv = Canvas(root, width=1000, height=500)
canv.pack()

canv.create_line(0,0,1000,500, fill='blue', dash=(4,4))
canv.create_line(1000,0,0,500)

canv.create_oval(50,50,500,500, fill='red')
canv.create_rectangle(10,10,200,300)

lista_slika = []

file = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")))
lista_slika.append(file)

dir = filedialog.askdirectory()
print(dir)

root.mainloop()
