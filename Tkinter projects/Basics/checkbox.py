from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learning checkbox')
root.geometry('400x400')
# Checkbutton requires variable to determine its type, IntVar or StringVar
var = StringVar()
# Default value for onvalue is 1 & for offvalue is 0
chut = Checkbutton(root, text='Check it!, or get fucked in the ass!'\
                   , variable=var, onvalue='Leave me alone', offvalue='Fuck me pls')
chut.deselect()          # Because of some glich in tkinter
chut.pack()

def value():
    Label(root, text=var.get()).pack()

Button(root, text='Show value', command=value).pack()
Button(root, text='Exit', command=root.quit, width=15).pack(pady=10)

root.mainloop()