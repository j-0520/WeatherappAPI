import requests
import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox
from urllib.request import urlopen
import json 
import os 
from dotenv import load_dotenv

load_dotenv(".env")
api_key = os.getenv("WEATHER_API_KEY")
weather_api = "https://www.meteosource.com/api/v1/free/point"
#place_id = input("what is the place you want the weather for: ")
#weather_params = {"place_id": place_id}
#weather_headers = {"X-API-Key": api_key}
#response_json = requests.get(weather_api, headers=weather_headers, params=weather_params)
#print(response_json.text)

# Tkinter GUI setup 
def get_weather(place_id: str) -> dict:
    url = "https://www.meteosource.com/api/v1/free/point" 
    weather_headers = {"X-API-Key": api_key}
    weather_params = {"place_id": place_id}
    response = requests.get(url, headers=weather_headers, params=weather_params)
    return response.json()
    

def on_get_weather():
    place_id = place_entry.get()
    if not place_id:
        messagebox.showerror("You haven't entered a place yet, Chuck one in.")
        return
    try:
        weather_data = get_weather(place_id)
        print(weather_data)
        #need to get this to print inside the window not in terminal
        window=tk.Tk()
        window.title("Weather Data")  
        weather_output = tk.Text(window)
        weather_output.pack()
        weather_output.insert("1.0", str(weather_data))
        window.mainloop()
        
        
    except Exception as e:
        messagebox.showerror("Error", f"Failed to get weather data: {e}")
        
window = tk.Tk()
window.title("Weather App")
window.resizable(width=True, height=True)

place_var = tk.StringVar()
place_entry = ttk.Entry(master=window, textvariable=place_var, text="Enter Desired location")
button_grabweather = tk.Button(master=window, text="Search")
#what I need to do here is make the text box grab the input and make it search for that place
button_grabweather.config(command=on_get_weather)



place_entry.pack()
button_grabweather.pack()

window.mainloop()   