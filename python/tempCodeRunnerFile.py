import requests
import tkinter as tk
from tkinter import messagebox

def get_food_tips(weather_desc):
    if "rain" in weather_desc.lower():
        return "Comfort foods like soups and hot chocolate are great on rainy days."
    elif "clear" in weather_desc.lower() or "sunny" in weather_desc.lower():
        return "Enjoy refreshing salads and smoothies in hot weather."
    else:
        return "How about some hearty stews to warm you up?"
def get_hydration_tips(temp):
    if temp > 30:
        return "Stay hydrated! Drink plenty of water and eat hydrating fruits like watermelon."
    elif temp < 10:
        return "Drink warm beverages like herbal teas to keep hydrated."
    else:
        return "Keep your hydration levels steady with regular water intake."

def get_emergency_kit():   # ye un jagh ke liye jaha cyclone ane ke jada possibility hai ya current weather my cyclone hit kar raha hai
    return [
        "1. Water (one gallon per person per day for at least three days)",
        "2. Non-perishable food (three-day supply)",
        "3. Flashlight and extra batteries",
        "4. First-aid kit",
        "5. Whistle to signal for help",
        "6. Dust mask to help filter contaminated air",
        "7. Multi-tool or knife",
        "8. Local maps",
        "9. Cell phone with chargers and a backup battery"
    ]
def get_clothing_recommendation(temp, weather_desc):
    if "rain" in weather_desc.lower():
        return "Don't forget an umbrella and wear waterproof shoes!"
    elif temp < 10:
        return "Wear a heavy coat and warm clothing."
    elif 10 <= temp < 20:
        return "A light jacket or sweater is recommended."
    else:
        return "You can wear summer clothing."
def get_weather():
    city = city_entry.get().strip().title()  
    API_KEY = '0573ba5a4dea522b4e4632c80a7f9de0'  
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'

    try:
        response = requests.get(url)
        data = response.json()

        if data['cod'] == 200:
            temperature = data['main']['temp']
            weather_desc = data['weather'][0]['description']
            recommendation = get_clothing_recommendation(temperature, weather_desc)
            food_tips = get_food_tips(weather_desc)
            hydration_tips = get_hydration_tips(temperature)
            emergency_kit = get_emergency_kit() if "cyclone" in weather_desc.lower() else []

           
            result_text = (
                f'Temperature: {temperature}°C\n'
                f'Weather: {weather_desc}\n'
                f'Recommendation: {recommendation}\n\n'
                f'Food Tips: {food_tips}\n\n'
                f'Hydration Tips: {hydration_tips}\n\n'
                f'Emergency Kit:\n' + '\n'.join(emergency_kit) if emergency_kit else "No emergency kit needed."
            )
            result_label.config(text=result_text)
        else:
            messagebox.showerror("Error", "City not found. Please check the name.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


root = tk.Tk()  
root.title("Weather-Based Clothing Recommendation")

city_label = tk.Label(root, text="Enter City:")  # Yeha pe city name 
city_label.pack()

city_entry = tk.Entry(root)  # User ke liye input jo gui me ayega
city_entry.pack()

get_weather_button = tk.Button(root, text="Get Recommendation", command=get_weather)  # button hai weather dekhne ke liye
get_weather_button.pack()

result_label = tk.Label(root, text="")  # jo "sabse impotant" hai result
result_label.pack()

root.mainloop()  # function call for gui loop