import requests
import tkinter as tk
from tkinter import messagebox

# Get your OpenWeatherMap API key and replace 'YOUR_API_KEY' below.
API_KEY ='0573ba5a4dea522b4e4632c80a7f9de0'

# Define clothing recommendations based on temperature ranges
def get_clothing_recommendation(temp):
    if temp < 0:
        return "Heavy winter coat, thermal wear, scarf, gloves, and winter boots."
    elif 0 <= temp < 10:
        return "Winter jacket, sweater, warm pants, and a beanie."
    elif 10 <= temp < 20:
        return "Light jacket, long sleeves, and jeans."
    elif 20 <= temp < 30:
        return "T-shirt, light pants or shorts, and a hat."
    else:
        return "Shorts, a tank top, sunglasses, and comfortable shoes."

# Function to fetch weather data
def fetch_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        
        if data["cod"] != 200:
            messagebox.showerror("Error", f"City not found: {city}")
            return None, None
        
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        
        return temp, weather
    except Exception as e:
        messagebox.showerror("Error", "Failed to retrieve weather data.")
        return None, None

# Function to display recommendations based on weather data
def show_recommendation():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    temp, weather = fetch_weather(city)
    if temp is not None:
        clothing = get_clothing_recommendation(temp)
        result_label.config(text=f"Weather: {weather.capitalize()}\nTemperature: {temp}°C\nRecommended clothing: {clothing}")

# Create GUI
app = tk.Tk()
app.title("Weather-Based Clothing Recommendation")
app.geometry("400x300")

# City input
city_label = tk.Label(app, text="Enter City:")
city_label.pack(pady=5)
city_entry = tk.Entry(app, width=25)
city_entry.pack(pady=5)

# Get recommendation button
recommend_button = tk.Button(app, text="Get Recommendation", command=show_recommendation)
recommend_button.pack(pady=10)

# Display result
result_label = tk.Label(app, text="", wraplength=350, justify="left")
result_label.pack(pady=10)

app.mainloop()
