import tkinter as tk
from tkinter import messagebox
import os

def move_file():
    source = source_entry.get()
    destination = destination_entry.get()

    try:
        if os.path.exists(destination):
            messagebox.showinfo("File Exists", "There is already a file at the destination.")
        else:
            os.replace(source, destination)
            messagebox.showinfo("File Moved", f"{source} was moved to {destination}.")
    except FileNotFoundError:
        messagebox.showerror("Error", f"{source} was not found.")

# Create the main application window
root = tk.Tk()
root.title("File Mover")

# Create labels and entry widgets for source and destination paths
source_label = tk.Label(root, text="Source Path:")
source_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
source_entry = tk.Entry(root, width=50)
source_entry.grid(row=0, column=1, padx=5, pady=5)
source_entry.insert(0, "C:\\Users\\User\\PycharmProjects\\Projects for YT shorts\\Text Files\\TestText.txt")

destination_label = tk.Label(root, text="Destination Path:")
destination_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
destination_entry = tk.Entry(root, width=50)
destination_entry.grid(row=1, column=1, padx=5, pady=5)
destination_entry.insert(0, "C:\\Users\\User\\PycharmProjects\\Projects for YT shorts\\Text Files\\Inner text files folder\\TestText.txt")

# Create a button to trigger file moving
move_button = tk.Button(root, text="Move File", command=move_file)
move_button.grid(row=2, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()
