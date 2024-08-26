import requests
import tkinter as tk
from tkinter import messagebox

def get_weather():
    city = entry_city.get()
    if city:
        try:
            url = f"http://wttr.in/{city}?format=%t+%C+%w"
            response = requests.get(url)
            if response.status_code == 200:
                weather_info = response.text.strip()
                update_weather_label(weather_info)
                update_weather_icon(weather_info)
            else:
                messagebox.showerror("Error", "City not found!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch weather data: {str(e)}")
    else:
        messagebox.showwarning("Warning", "Please enter a city.")

def update_weather_label(weather_info):
    weather_label.config(text=weather_info)

def update_weather_icon(weather_info):
    weather_desc = weather_info
    if "cloud" in weather_desc.lower():
        weather_icon_path = "cloud.png"
    elif "rain" in weather_desc.lower():
        weather_icon_path = "rainycloud.png"
    elif "sun" in weather_desc.lower() or "clear" in weather_desc.lower():
        weather_icon_path = "sun.png"
    else:
        weather_icon_path = "notavailable.png"

    # Load the weather icon
    weather_icon = tk.PhotoImage(file=weather_icon_path)

    # Update the weather icon on the GUI
    weather_icon_label.config(image=weather_icon)
    weather_icon_label.image = weather_icon

root = tk.Tk()
root.title("Weather Forecast")
root.resizable(False, False)

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

label_city = tk.Label(frame, text="City:")
label_city.grid(row=0, column=0)

entry_city = tk.Entry(frame, width=30)
entry_city.grid(row=0, column=1)

button_get_weather = tk.Button(frame, text="Get Weather", command=get_weather)
button_get_weather.grid(row=0, column=2, padx=5)

weather_label = tk.Label(root, text="")
weather_label.pack(pady=10)

# Create a label to display the weather icon
weather_icon_label = tk.Label(root)
weather_icon_label.pack(pady=10)

root.mainloop()
