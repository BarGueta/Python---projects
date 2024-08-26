import tkinter as tk
from tkinter import messagebox
import webbrowser
from geopy.geocoders import Nominatim
import random

class RandomLocationGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Location Generator")

        self.label = tk.Label(root, text="Click the button to generate a random location:")
        self.label.pack()

        self.coordinates_label = tk.Label(root, text="")
        self.coordinates_label.pack()

        self.location_label = tk.Label(root, text="")
        self.location_label.pack()

        self.map_button = tk.Button(root, text="Show on Map", command=self.show_on_map, padx=10, pady=10)
        self.map_button.pack()

        self.generate_button = tk.Button(root, text="Generate", command=self.generate_location, padx=10, pady=10)
        self.generate_button.pack()

    def generate_location(self):
        latitude = random.uniform(-90, 90)
        longitude = random.uniform(-180, 180)
        coordinates = f"Latitude: {latitude}, Longitude: {longitude}"
        self.coordinates_label.config(text=coordinates)
        self.coordinates_label.config(background="grey")

        geolocator = Nominatim(user_agent="random_location_generator")
        location = geolocator.reverse((latitude, longitude))
        if location is not None:
            self.location_label.config(text="Location: " + location.address)
            self.location_label.config(background="grey")
            self.latitude = latitude
            self.longitude = longitude
        else:
            self.location_label.config(text="Location not found for given coordinates.")
            self.location_label.config(background="grey")
            self.latitude = None
            self.longitude = None

    def show_on_map(self):
        if self.latitude is not None and self.longitude is not None:
            map_url = f"https://www.openstreetmap.org/?mlat={self.latitude}&mlon={self.longitude}#map=15/{self.latitude}/{self.longitude}"
            webbrowser.open_new_tab(map_url)
        else:
            tk.messagebox.showerror("Error", "Location not found.")

if __name__ == "__main__":
    root = tk.Tk()
    #root.geometry("500x300")
    app = RandomLocationGenerator(root)
    root.mainloop()
