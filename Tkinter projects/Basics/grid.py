from tkinter import *

root = Tk()
# Creating label
myLabel = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My name is Sumedh, nice to meet you!")
# Shoving it onto screen
myLabel.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)
root.mainloop()
