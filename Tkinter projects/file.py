from tkinter import *
from PIL import Image,ImageTk
from tkinter import filedialog

root = Tk()
root.title('How to open a file')
root.iconbitmap('images/icons/folder.ico')

def open():
    global myImg
    root.filename = filedialog.askopenfilename(initialdir="C:/Users/Sumedh/PycharmProjects/Tkinter projects/images",\
                                               title="Open folder", filetypes=(("jpeg files", "*.jpeg"),("all files", "*.*")))
    myImg = ImageTk.PhotoImage(Image.open(root.filename))
    Label(image=myImg).pack()

btn = Button(root, text='Open a file', command=open).pack(pady=10)
Button(root, text='Exit', command=root.quit, width=15).pack(pady=10)

root.mainloop()