from tkinter import *
from PIL import Image, ImageTk
import requests
import json

root = Tk()
root.title('Air Quality Index')
root.iconbitmap('C:/Users/Sumedh/PycharmProjects/Tkinter projects/images/icons/earth.ico')
root.geometry('450x130')

# My API url for reference
# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=10001&distance=5&API_KEY=00F872E0-395F-4206-B2BA-3575368D17F9

def delete_text():
    my_label.destroy()
    zip.delete(0, END)
    zip_button['state'] = NORMAL
# Create a function to lookup zipcode
def zipLookup():
    try:
        global my_label

        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=5&API_KEY=00F872E0-395F-4206-B2BA-3575368D17F9")
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']
        # To display resp colors for each category
        if category == 'Good':
            weather_color = '#2CF32E'
        elif category == 'Moderate':
            weather_color = '#F9FF30'
        elif category == 'Unhealthy for Sensitive Groups':
            weather_color = '#FF9200'
        elif category == 'Unhealthy':
            weather_color = '#EF1010'
        elif category == 'Very Unhealthy':
            weather_color = '#81039A'
        elif category == 'Hazardous':
            weather_color = '#790866'

        root.configure(background=weather_color)
        my_label = Label(root, text=city + ', ' + 'Air Quality: ' + str(quality) + ', ' + category, font=("Helvetica", 15), background=weather_color)
        my_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        del_button = Button(root, text='Delete', command=delete_text)
        del_button.grid(row=2, column=0,columnspan=2, padx=10, pady=8, ipadx=80)

        zip_button['state'] = DISABLED
    except Exception as e:
        api = 'Error...'

zip = Entry(root, font=('Helvetica', 13))
zip.grid(row=0, column=0,padx=10, sticky=W+E)
zip_button = Button(root, text='Lookup Zipcode', command=zipLookup)
zip_button.grid(row=0, column=1, sticky=W+E+N+S, padx=10, pady=10)

root.mainloop()
'''
10001: New York City, NY
90210: Beverly Hills, California. 
33162: Miami, Florida. 
60606: Chicago, Illinois.
42748: Hodgenville, Kentucky. 
70130: New Orleans, Louisiana.
48202: Detroit, Michigan.
'''
