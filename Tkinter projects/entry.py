from tkinter import *
root = Tk()

# to create input box
e = Entry(root, width=30)
e.pack()
e.insert(0,"Enter Your Name:")

def Button1():
    hello = "Hello! " + e.get()
    label1 = Label(root, text=hello)
    label1.pack()

# to create and display button
# remember not use () after calling a function here
myButton1 = Button(root, text="OK", command= Button1, padx=25)
myButton1.pack()

e2 = Entry(root, width=30)
e2.pack()
e2.insert(0,"Email ID:")

def Button2():
    label1 = Label(root, text=e2.get())
    label1.pack()

myButton2 = Button(root, text="OK", command=Button2, padx=25)
myButton2.pack()

root.mainloop()

