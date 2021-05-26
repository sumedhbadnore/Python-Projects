from tkinter import *

root = Tk()
root.title('Frame in Tkinter')
root.iconbitmap('images/icons/arrow.ico')

frame = LabelFrame(root, text='This is my frame!', padx=40, pady=40)   # To distant from inside of the frame
frame.pack(padx=20, pady=20)   # To distant form outside of frame

# You can use pack and grid simultaneously in frame
b = Button(frame, text="Don't click here!", command=root.quit)
b2 = Button(frame, text="...or here")
b.grid(row=0, column=0, pady=10)
b2.grid(row=1, column=0)


root.mainloop()