from tkinter import *

root = Tk()
root.title('How to use dropdown box')
root.geometry('400x400')

options = [
    "Lunday",
    "Chutday",
    "Ganday",
    "Boobday",
    "Jhhatay"
]
# Just like checkboxes, dropdown box requires variable type, IntVar or StringVar
select = StringVar()
select.set(options[0])

# To use list we've to use * infornt of list name
drop = OptionMenu(root, select, *options)
drop.pack()

def show():
    Label(root, text=select.get()).pack()

my_button = Button(root, text='Show value', command=show).pack()

Button(root, text='Exit', command=root.quit, width=15).pack()
root.mainloop()