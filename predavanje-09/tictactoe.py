from tkinter import *

from tkinter import messagebox


root = Tk()
root.title('Tic tac toe GUI')

button_1 = Button(root, text='X', height=5, width=7, command=lambda: button_is_clicked(button_1), bg='#48BECC', fg='white')
button_2 = Button(root, text='', height=5, width=7, command=lambda: button_is_clicked(button_2))
button_3 = Button(root, text='', height=5, width=7, command=lambda: button_is_clicked(button_3))
button_4 = Button(root, text='', height=5, width=7, command=lambda: button_is_clicked(button_4))
button_5 = Button(root, text='', height=5, width=7, command=lambda: button_is_clicked(button_5))
button_6 = Button(root, text='', height=5, width=7, command=lambda: button_is_clicked(button_6))
button_7 = Button(root, text='', height=5, width=7, command=lambda: button_is_clicked(button_7))
button_8 = Button(root, text='', height=5, width=7, command=lambda: button_is_clicked(button_8))
button_9 = Button(root, text='', height=5, width=7, command=lambda: button_is_clicked(button_9))

button_1.grid(row=0, column=0)
button_2.grid(row=0, column=1)
button_3.grid(row=0, column=2)
button_4.grid(row=1, column=0)
button_5.grid(row=1, column=1)
button_6.grid(row=1, column=2)
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

def get_button_position(button_string):
    button_string = str(button_string)
    translator = {
        '.!button':1,
        '.!button2':2,
        '.!button3':3,
        '.!button4':4,
        '.!button5':5,
        '.!button6':6,
        '.!button7':7,
        '.!button8':8,
        '.!button9':9
    }
    return translator[button_string]

def button_is_clicked(button_name):
    # button_name.config(bg='red')
    print(button_name['bg'])
    print(get_button_position(button_name))




root.mainloop()