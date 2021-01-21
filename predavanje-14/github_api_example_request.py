import requests
import json
import tkinter

response = requests.get('https://api.github.com/users/nikolakadic')

user_name = response.json()['name']

root = tkinter.Tk()

root.title(user_name)

root.mainloop()