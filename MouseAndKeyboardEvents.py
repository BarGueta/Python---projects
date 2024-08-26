import tkinter as tk

def key(event):
    """Function to handle key press events"""
    print("Key pressed:", repr(event.keysym))
    info_label.config(text="Key pressed: " + repr(event.keysym))

def callback(event):
    """Function to handle mouse click events"""
    frame.focus_set()
    print("Clicked at:", event.x, event.y)
    info_label.config(text = "Clicked at: " + str(event.x) + ", " + str(event.y))

# Create the main window
root = tk.Tk()
root.title("Key Events Example")
root.geometry("500x500")

info_label = tk.Label(font=("Arial", 20))
info_label.pack()

# Create a frame to capture key events
frame = tk.Frame(root, width=500, height=500, background="grey")
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.pack()

# Run the Tkinter event loop
root.mainloop()
