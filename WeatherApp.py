from tkinter import *
import requests
import urllib.parse

API_KEY = "60e461bdb861deec3c66fecc3fe7058f"


def get_weather():
    city_raw = city_entry.get().strip()
    city = urllib.parse.quote(city_raw.title())
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        result = (f"City: {city_raw.title()}\nTemperature: {temp}°C\nCondition: {desc.title()}")
    else:
        result = "❌ City not found!"

    result_label.config(text=result)


root = Tk()
root.title("Weather App")
root.geometry("400x400")

city_entry = Entry(root, font=("Arial", 16))
city_entry.pack(pady=10)

search_btn = Button(root, text="Get Weather", command=get_weather, font=("Arial", 14))
search_btn.pack(pady=20)

result_label = Label(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

root.mainloop()