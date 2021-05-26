from tkinter import*
from PIL import ImageTk, Image

root = Tk()
root.title('Say Cheese!')
root.iconbitmap('images/icons/arrow.ico')

my_img = ImageTk.PhotoImage(Image.open('images/5.jpeg'))
my_label = Label(image=my_img)
my_label.pack()

button_quit = Button(root, text='Exit', command=root.quit, padx=20)
button_quit.pack()

root.mainloop()
