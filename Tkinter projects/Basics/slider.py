from tkinter import*
from PIL import ImageTk, Image

root = Tk()
root.title('Slider')
root.iconbitmap('images/icons/groot.ico')
root.geometry("400x400")

def slide(var):
    Label(root, text='horizontal='+ str(hslider.get())).pack()
    Label(root, text='vertical=' + str(vslider.get())).pack()
    root.geometry(str(hslider.get()) + "x" + str(vslider.get()))

vslider = Scale(root, from_=0, to=400, command=slide)
vslider.pack()

hslider = Scale(root, from_=0, to=400, orient=HORIZONTAL, command=slide)
hslider.pack()

btn = Button(root, text='Resize Window', command=slide).pack(pady=10)
Button(root, text='Exit', command=root.quit, width=12).pack(pady=10)

root.mainloop()