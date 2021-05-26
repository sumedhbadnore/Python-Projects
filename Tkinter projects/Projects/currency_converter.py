# Real Time Currency Converter using API By: Sumedh, Mandar, Aniket, Pranjan
# API link https://api.exchangerate-api.com/v4/latest/USD

import requests
from tkinter import *
from tkinter import ttk


class RealTimeCurrencyConverter():
    def __init__(self,url):
            self.data = requests.get(url).json()
            self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount 
        if from_currency != 'USD' : 
            amount = amount / self.currencies[from_currency] 
  
        # limiting the precision to 4 decimal places 
        amount = round(amount * self.currencies[to_currency], 4) 
        return amount

class App(Tk):

    def __init__(self, converter):
        Tk.__init__(self)
        self.title('Currency Converter')
        self.iconbitmap('C:/Users/Sumedh/PycharmProjects/Tkinter projects/images/icons/green_lantern.ico')
        self.currency_converter = converter

        #self.configure(background = 'blue')
        self.geometry("500x200")
        
        # Label
        self.intro_label = Label(self, text = 'Real Time Currency Converter',  fg = 'green', borderwidth = 2)
        self.intro_label.config(font = ('Times New Roman',18,'bold'))

        self.date_label = Label(self, text = f"1 USD equals = {self.currency_converter.convert('USD','INR',1)} INR \n Date : {self.currency_converter.data['date']}", borderwidth = 5)
        self.date_label.config(font =('Arial',12))

        self.intro_label.place(x = 90 , y = 5)
        self.date_label.place(x = 155, y= 50)

        # Entry box
        self.amount_field = Entry(self,bd = 3, relief = RIDGE, justify = CENTER)
        self.converted_amount_field_label = Label(self, text = '', fg = 'black', bg = 'white', relief = RIDGE, justify = CENTER, width = 17, borderwidth = 3)

        # dropdown
        self.from_currency_variable = StringVar(self)
        self.from_currency_variable.set("INR") # default value
        self.to_currency_variable = StringVar(self)
        self.to_currency_variable.set("USD") # default value

        font = ("Courier", 12, "bold")
        self.option_add('*TCombobox*Listbox.font', font)
        self.from_currency_dropdown = ttk.Combobox(self, textvariable=self.from_currency_variable,values=list(self.currency_converter.currencies.keys()), font = font, state = 'readonly', width = 12, justify = CENTER)
        self.to_currency_dropdown = ttk.Combobox(self, textvariable=self.to_currency_variable,values=list(self.currency_converter.currencies.keys()), font = font, state = 'readonly', width = 12, justify = CENTER)

        # placing
        self.from_currency_dropdown.place(x = 30, y= 120)
        self.amount_field.place(x = 36, y = 150)
        self.to_currency_dropdown.place(x = 340, y= 120)
        #self.converted_amount_field.place(x = 346, y = 150)
        self.converted_amount_field_label.place(x = 346, y = 150)
        
        # Convert button
        self.convert_button = Button(self, text = "Convert", fg = "black", command = self.perform) 
        self.convert_button.config(font=('Courier', 10, 'bold'))
        self.convert_button.place(x = 225, y = 135)

    def perform(self):
        try:
            amount = float(self.amount_field.get())
            from_curr = self.from_currency_variable.get()
            to_curr = self.to_currency_variable.get()

            converted_amount = self.currency_converter.convert(from_curr,to_curr,amount)
            converted_amount = round(converted_amount, 2)

            self.converted_amount_field_label.config(text = str(converted_amount))
        except Exception as e:  
            print('Error Occured, Please Input Float Value')
            print(e)
            
if __name__ == '__main__':
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    converter = RealTimeCurrencyConverter(url)

    App(converter)
    mainloop()

