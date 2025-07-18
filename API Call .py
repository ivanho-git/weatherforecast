from tkinter import *
from tkinter import ttk
import requests
from PIL import Image, ImageTk
import io


def get_weather():
    city = city_var.get()
    try:
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=9a4a25a970140e7ade2156bf516a135f"
        )
        data = response.json()

        if data.get("cod") != 200:
            raise Exception(data.get("message", "City not found"))

        # Extract weather data
        weather_main.set(data["weather"][0]["main"])
        description.set(data["weather"][0]["description"].title())
        temp_c = data["main"]["temp"] - 273.15
        temperature.set(f"{temp_c:.2f} °C")
        pressure.set(f"{data['main']['pressure']} hPa")

        # Set icon
        icon_code = data["weather"][0]["icon"]
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
        icon_response = requests.get(icon_url)
        icon_img = Image.open(io.BytesIO(icon_response.content)).resize((100, 100))
        icon_tk = ImageTk.PhotoImage(icon_img)
        icon_label.config(image=icon_tk)
        icon_label.image = icon_tk

        status_bar.config(text=f"✅ Weather for {city.title()} fetched successfully!")

    except Exception as e:
        weather_main.set("❌ Error")
        description.set("Invalid City Name")
        temperature.set("N/A")
        pressure.set("N/A")
        status_bar.config(text=f"⚠️ {str(e)}")
