from tkinter import *
from tkinter import messagebox  # imp to use messagebox

root = Tk()
root.title('Message boxes')
root.iconbitmap('images/icons/arrow.ico')

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
def popup():
    response = messagebox.askquestion("This is my message", "Are you going to start studying now?")
    if response == 'yes':                               # Only for 'askquestion' it returns yes/no
        Label(root, text='Great! proud of you').pack()     # for others it returns 1/0
    else:
        Label(root, text='Fuck off!').pack()

Button(root, text='Popup!', command=popup).pack()

root.mainloop()