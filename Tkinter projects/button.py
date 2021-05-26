
from tkinter import *
root = Tk()
# to show after button is clicked
def myClick():
    label1 = Label(root, text="Look you clicked the button!")
    label1.pack()
def myClick2():
    label = Label(root, text="Now don't over do it -_-")
    label.pack()

# to create and display button
# remember not use () after calling a function here
myButton = Button(root, text="Click me!", command= myClick)
myButton2 = Button(root, text="Click me!", command= myClick2, fg='white', bg='purple',padx = 50, pady=10)
myButton.pack()
myButton2.pack()

root.mainloop()
