import tkinter as tk
from tkinter import messagebox

def on_button_click():
    messagebox.showinfo("Button Clicked", "You clicked the button!")

# Create the main window
root = tk.Tk()
root.title("Custom Button Example")
root.geometry("300x200")

# Customize the button
button = tk.Button(
    root,
    text="Click Me",          # Button text
    command=on_button_click,  # Function to call when button is clicked
    fg="white",               # Text color
    bg="blue",                # Background color
    font=("Helvetica", 14),   # Font type and size
    relief="raised",          # Button relief type (flat, raised, sunken, groove, ridge)
    bd=5,                     # Border width
    padx=10,                  # Padding in the x direction
    pady=5                    # Padding in the y direction
)

# Place the button in the window
button.pack(pady=20)

# Start the main event loop
root.mainloop()
