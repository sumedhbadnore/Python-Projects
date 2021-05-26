from tkinter import *


root = Tk()
root.title('Pizza Selection')
root.iconbitmap('images/icons/arrow.ico')

# List for mode of radio button
TOPPINGS = [
    ("Margharita","Margharita"),
    ("Double Cheese","Double Cheese"),
    ("Paneer","Paneer"),
    ("Onion","Onion"),
    ("Cheese Burst","Cheese Burst")
]

# Radio button requires variable type, StringVar or IntVar
pizza = StringVar()
pizza.set("Cheese Burst")

# Loop for each radio button
for text, topping in TOPPINGS:
    Radiobutton(root, text=text, variable=pizza, value=topping).pack(anchor=W)

# To show what happens after clicking my_button
def clicked(value):
    my_label = Label(root, text=value)
    my_label.pack()

# To print which pizza has been selected
my_button = Button(root, text='Click me!', command=lambda: clicked(pizza.get()))
my_button.pack()

# To exit prog
b = Button(root, text='Exit', command=root.quit).pack()
root.mainloop()