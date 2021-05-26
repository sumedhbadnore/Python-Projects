from tkinter import *
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title("To Plot Graph")
root.iconbitmap("images/icons/bulb.ico")
root.geometry("400x400")

def graph():
    house_prices = np.random.normal(200000, 25000, 5000)
    plt.hist(house_prices, 30)
    plt.show()

my_button = Button(root, text='Plot graph', command=graph)
my_button.pack()

root.mainloop()