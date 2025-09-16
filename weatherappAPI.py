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
place_id = input("what is the place you want the weather for: ")
weather_params = {"place_id": place_id}
weather_headers = {"X-API-Key": api_key}
response_json = requests.get(weather_api, headers=weather_headers, params=weather_params)
print(response_json.text)

# Tkinter GUI setup 