from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.title('To create new window')
root.iconbitmap('images/icons/arrow.ico')

def open():
    global img
    win1 = Toplevel()
    root.title('My new window')
    img = ImageTk.PhotoImage(Image.open("images/3.jpeg"))
    Label(win1, image=img).pack()
    Button(win1, text='Exit', command=win1.destroy).pack()

b = Button(root, text='New window', command=open).pack()
root.mainloop()