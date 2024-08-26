import tkinter as tk

def update_value():
    value_label.config(text="Selected value: " + str(spinbox.get()))

# Create the main application window
root = tk.Tk()
root.title("Spinbox Example")
root.geometry("300x150")
root.resizable(False, False)

# Create a Spinbox widget
spinbox = tk.Spinbox(root, from_=0, to=100, width=10)
spinbox.pack(pady=10)

# Create a label to display the selected value
value_label = tk.Label(root, text="Selected value: ")
value_label.pack()

# Create a button to update the value label
update_button = tk.Button(root, text="Update", command=update_value)
update_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
