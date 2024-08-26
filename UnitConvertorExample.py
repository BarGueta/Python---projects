import tkinter as tk
from tkinter import ttk

def convert():
    try:
        value = float(entry.get())
        unit = variable.get()

        if unit == "Feet to Meters":
            result = value * 0.3048
        elif unit == "Meters to Feet":
            result = value * 3.28084
        elif unit == "Pounds to Kilograms":
            result = value * 0.453592
        elif unit == "Kilograms to Pounds":
            result = value * 2.20462
        else:
            result = "Invalid conversion"

        result_label.config(text=str(result))
    except ValueError:
        result_label.config(text="Invalid input")

# Create main window
root = tk.Tk()
root.resizable(False, False)
root.title("Unit Converter")

# Create input entry
entry = tk.Entry(root, width=10)
entry.grid(row=0, column=0, padx=5, pady=5)

# Create dropdown menu for unit selection
units = ["Feet to Meters", "Meters to Feet", "Pounds to Kilograms", "Kilograms to Pounds"]
variable = tk.StringVar(root)
variable.set(units[0])  # default value

dropdown = ttk.Combobox(root, textvariable=variable, values=units)
dropdown.grid(row=0, column=1, padx=5, pady=5)

# Create convert button
convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.grid(row=0, column=2, padx=5, pady=5)

# Create label to display result
result_label = tk.Label(root, text="")
result_label.grid(row=1, columnspan=3, padx=5, pady=5)

root.mainloop()
