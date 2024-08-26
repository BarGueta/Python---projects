import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Frame Example")
root.geometry("800x400")
root.resizable(False, False)

# Create a frame
frame = tk.Frame(root, bg="lightgray", bd=5, relief=tk.SUNKEN)
frame.pack(padx=20, pady=20)

# Add widgets to the frame
label = tk.Label(frame, text="All widgets, including this label are in one frame (Frame stores widgets within it)", bg="lightgray")
label.pack(padx=10, pady=10)

button = tk.Button(frame, text="Click me!", command=lambda: entry.insert(0, "Button is clicked"))
button.pack(padx=10, pady=10)

entry = tk.Entry(frame)
entry.pack(padx=10, pady=10)

# Run the Tkinter event loop
root.mainloop()
