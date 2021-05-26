from tkinter import*
from PIL import ImageTk, Image

root = Tk()
root.title('Image Viewer')
root.iconbitmap('C:/Users/Sumedh/PycharmProjects/Tkinter projects/images/icons/Gallery.ico')

# Images to be displayed
my_img1 = ImageTk.PhotoImage(Image.open('C:/Users/Sumedh/PycharmProjects/Tkinter projects/images/1.jpg'))
my_img2 = ImageTk.PhotoImage(Image.open('C:/Users/Sumedh/PycharmProjects/Tkinter projects/images/2.JPG'))
my_img3 = ImageTk.PhotoImage(Image.open('C:/Users/Sumedh/PycharmProjects/Tkinter projects/images/3.jpeg'))
my_img4 = ImageTk.PhotoImage(Image.open('C:/Users/Sumedh/PycharmProjects/Tkinter projects/images/4.jpeg'))
my_img5 = ImageTk.PhotoImage(Image.open('C:/Users/Sumedh/PycharmProjects/Tkinter projects/images/5.jpeg'))
my_img6 = ImageTk.PhotoImage(Image.open('C:/Users/Sumedh/PycharmProjects/Tkinter projects/images/6.jpeg'))
my_img7 = ImageTk.PhotoImage(Image.open('C:/Users/Sumedh/PycharmProjects/Tkinter projects/images/7.jpg'))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5, my_img6, my_img7]

# Display first image
my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

status = Label(root, text='Image 1 of ' + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

def back(img_number):
    global my_label
    global button_back
    global button_forward

    my_label.grid_forget()
    my_label = Label(image=image_list[img_number - 1])  # This img will be displayed
    button_forward = Button(root, text='>>', command=lambda: forward(img_number + 1))  # When forward button is pressed
    button_back = Button(root, text='<<', command=lambda: back(img_number - 1))  # When back button is pressed

    if img_number == 1:
        button_back = Button(root, text='>>', state=DISABLED)
    # To update status bar
    # anchor to put text on East (right) side     bd is border   relief to sunk the label
    status = Label(root, text='Image ' + str(img_number) + ' of ' + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0, padx=40)
    button_forward.grid(row=1, column=2, padx=40)

def forward(img_number):
    global my_label
    global button_back
    global button_forward

    my_label.grid_forget()
    my_label = Label(image=image_list[img_number-1])         #This img will be displayed
    button_forward = Button(root, text='>>', command=lambda: forward(img_number+1))    # When forward button is pressed
    button_back = Button(root, text='<<', command=lambda: back(img_number-1))  # When back button is pressed

    if img_number == 7:
        button_forward = Button(root, text='>>', state=DISABLED)
    # To update status bar
    status = Label(root, text='Image ' + str(img_number) + ' of ' + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0, padx=40)
    button_forward.grid(row=1, column=2, padx=40)

button_back = Button(root, text='<<', command=back, state=DISABLED)
button_quit = Button(root, text='Exit', command=root.quit, padx=20)
button_forward = Button(root, text='>>', command=lambda: forward(2))

button_back.grid(row=1, column=0,)
button_quit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10 )
status.grid(row=2, column=0, columnspan=3, sticky=W+E)  # sticky to extend label from West to East

root.mainloop()
