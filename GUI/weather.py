# -*- coding: utf-8 -*-
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog
import requests
import json

root = Tk()
root.title("Omg")
root.iconbitmap('icon.ico')
root.geometry("600x100")
myLabel = Label(root)


def zipLookup():
    zipcode.get()
    #zipLabel = Label(root, text = zipcode.get())
    #zipLabel.grid(row = 1, column = 0, columnspan = 2)

   

    
    try:
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode.get() + "&distance=5&API_KEY=824CBF5D-1DC7-4362-8F55-5D64E3C5456C")
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        
        if category == "Good":
            weather_color = "#00e400"
        elif category == "Moderate":
            weather_color = "#ffff00"
        elif category == "Unhealthy for Sensitive Groups":
            weather_color = "#ff7e00"
        elif category == "Unhealthy":
            weather_color = "#ff0000"
        elif category == "Very Unhealthy":
            weather_color = "#8f3f97"
        elif category == "Hazardous":
            weather_color = "#7e0023"
            
        root.configure(background = weather_color)
        myLabel.config(text = city + " Air Quality " + str(quality) + " " + category, font = ("Helvetica", 20), background = weather_color)
        myLabel.grid(row = 1, column = 0, columnspan = 2)


            
    except Exception as e:
        api = "error..."


    
zipcode = Entry(root)

zipcode.grid(row = 0, column = 0, stick = W+S+N+E)

zipBtn = Button(root, text = "Lookup Zipcode", command = zipLookup)
zipBtn.grid(row = 0, column = 1, stick = W+S+N+E)

root.mainloop()