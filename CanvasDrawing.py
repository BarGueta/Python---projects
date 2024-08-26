import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Drawing with Tkinter Canvas")

# Create a Canvas widget
canvas = tk.Canvas(root, width=400, height=300, bg="light green")
canvas.pack()

# Draw a rectangle on the canvas
rectangle = canvas.create_rectangle(50, 50, 200, 150, fill="blue")

# Draw a circle on the canvas
circle1 = canvas.create_oval(250, 50, 350, 150, fill="red")

# Draw a line on the canvas
line = canvas.create_line(100, 200, 300, 250, fill="green", width=3)

# Draw a circle
circle2 = canvas.create_oval(100, 200, 150, 250, fill="yellow")

# Draw a triangle
triangle = canvas.create_polygon(250, 200, 350, 200, 300, 150, fill="orange")

# Run the Tkinter event loop
root.mainloop()
