import tkinter as tk
from tkinter import ttk
import requests
import webbrowser
import folium


def track_flights():
    global flights_data  # Define global variable to store flight data
    url = "https://opensky-network.org/api/states/all"
    params = {}  # Empty params dictionary
    response = requests.get(url, params=params)
    if response.status_code == 200:
        flights_data = response.json()["states"]  # Store flight data
        display_flights(flights_data)
    else:
        print("Failed to retrieve flight data")


def display_flights(data):
    flight_info.config(state=tk.NORMAL)  # Enable editing temporarily
    flight_info.delete(1.0, tk.END)  # Clear previous data
    for i, flight in enumerate(data):
        icao24 = flight[0]
        callsign = flight[1]
        latitude = flight[6] if flight[6] is not None else "Unknown"
        longitude = flight[5] if flight[5] is not None else "Unknown"
        altitude = flight[7]
        origin = flight[2] if flight[2] else "Unknown"
        flight_info.insert(tk.END, f"{i + 1}. ICAO24: {icao24}, Callsign: {callsign}, Latitude: {latitude}, Longitude: {longitude}, Altitude: {altitude} meters, Origin: {origin}\n------------------"
                                   f"-----------------------------------------------------------------------------------------------------------------------\n")
    flight_info.config(state=tk.DISABLED)  # Make read-only again


def show_flight_location():
    row_number = flight_row_entry.get()
    try:
        row_number = int(row_number)
    except ValueError:
        print("Invalid row number")
        return

    if 1 <= row_number <= len(flights_data):
        selected_flight_index = row_number - 1
        selected_flight = flights_data[selected_flight_index]
        latitude = selected_flight[6]
        longitude = selected_flight[5]
        if latitude and longitude:
            # Open a web browser with a map showing the flight's location
            map = folium.Map(location=[latitude, longitude], zoom_start=8)
            folium.Marker([latitude, longitude], popup="Flight Location").add_to(map)
            map.save('flight_location.html')
            webbrowser.open('flight_location.html')
    else:
        print("Invalid row number")


def main():
    root = tk.Tk()
    root.title("Flight Tracker")
    root.resizable(False, False)

    label = tk.Label(root, text="Flight Tracker")
    label.pack()

    image = tk.PhotoImage(file="planelogo.png")  # Replace "example_image.png" with your image file path

    # Create a label to display the image
    logolabel = tk.Label(root, image=image)
    logolabel.pack()

    track_button = tk.Button(root, text="Update flight tracker", command=track_flights)
    track_button.pack()

    frame = ttk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True)

    vertical_scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL)
    vertical_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    horizontal_scrollbar = ttk.Scrollbar(frame, orient=tk.HORIZONTAL)
    horizontal_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

    global flight_info
    flight_info = tk.Text(frame, height=20, width=100, wrap=tk.NONE,
                          yscrollcommand=vertical_scrollbar.set,
                          xscrollcommand=horizontal_scrollbar.set)
    flight_info.pack(fill=tk.BOTH, expand=True)
    flight_info.config(state=tk.DISABLED)  # Make text area read-only

    vertical_scrollbar.config(command=flight_info.yview)
    horizontal_scrollbar.config(command=flight_info.xview)

    flight_row_label = tk.Label(root, text="Enter row number of flight:")
    flight_row_label.pack()

    global flight_row_entry
    flight_row_entry = tk.Entry(root)
    flight_row_entry.pack()

    show_location_button = tk.Button(root, text="Show most update location of a flight by row", command=show_flight_location)
    show_location_button.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
