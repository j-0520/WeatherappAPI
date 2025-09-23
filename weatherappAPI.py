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
    response.raise_for_status()
    return response.json()

def on_get_weather():
    place_id = place_var.get()
    if not place_id:
        messagebox.showerror("You haven't entered a place yet, Chuck one in.")
        return
    try:
        weather_data = get_weather(place_id)
        messagebox.showinfo("Weather Data")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to get weather data: {e}")
        
window = tk.Tk()
window.title("Weather App")
window.resizable(width=True, height=True)

place_var = tk.StringVar()
place_entry = ttk.Entry(master=window, textvariable=place_var)
button_grabweather = tk.Button(master=window, text="Search")
place_entry.pack()
button_grabweather.pack()

window.mainloop()   