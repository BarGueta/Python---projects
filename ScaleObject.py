import tkinter as tk

def scale_callback(value):
    info_label.config(text="Scale value:" + str(value))
    #print("Scale value:", value)

# Create the main window
root = tk.Tk()
root.geometry("300x300")
root.title("Scale Example")

# Create the Scale widget
scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=scale_callback)
scale.pack(pady=20)

info_label = tk.Label(root, font = ("Arial", 25))
info_label.place(relx = 0.5, rely = 0.5, anchor="center")

# Run the Tkinter event loop
root.mainloop()
