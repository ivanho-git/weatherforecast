from tkinter import *
from tkinter import ttk
import requests
from PIL import Image, ImageTk
import io


root = Tk()
root.title("🌦 Weather App")
root.geometry("600x550")
root.configure(bg="#2C3333")

LABEL_STYLE = {"font": ("Poppins", 12), "bg": "#2C3333", "fg": "white"}
ENTRY_STYLE = {"font": ("Poppins", 12), "bg": "#395B64", "fg": "white"}
BUTTON_STYLE = {"font": ("Poppins", 12, "bold"), "bg": "#00ADB5", "fg": "white", "bd": 0}

# ---------- Title ----------
title = Label(root, text="🌤️ Fancy Weather Forecast App", font=("Poppins", 20, "bold"), bg="#00ADB5", fg="white", pady=10)
title.pack(fill=X, pady=10)

# ---------- Dropdown ----------
form_frame = Frame(root, bg="#2C3333")
form_frame.pack(pady=10)

Label(form_frame, text="🌆 Enter City Name:", **LABEL_STYLE).grid(row=0, column=0, padx=10)

city_var = StringVar()
city_entry = Entry(form_frame, textvariable=city_var, **ENTRY_STYLE, width=25, relief=FLAT)
city_entry.grid(row=0, column=1, padx=10)

# ---------- Get Button ----------
get_btn = Button(form_frame, text="🔍 Get Weather", command=get_weather, **BUTTON_STYLE)
get_btn.grid(row=0, column=2, padx=10, ipadx=10, ipady=2)
