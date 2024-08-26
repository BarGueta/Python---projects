import tkinter as tk

def move(event):
    """Function to move the label"""
    if event.keysym == 'Up':
        canvas.move(label, 0, -5)
    elif event.keysym == 'Down':
        canvas.move(label, 0, 5)
    elif event.keysym == 'Left':
        canvas.move(label, -5, 0)
    elif event.keysym == 'Right':
        canvas.move(label, 5, 0)

# Create the main window
root = tk.Tk()
root.title("Move Label Example")
root.resizable(False, False)

# Create a canvas
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

# Create a red label
label = canvas.create_text(150, 150, text="Move Me", fill="red", font=('Arial', 12))

# Bind arrow key events to the move function
root.bind("<Up>", move)
root.bind("<Down>", move)
root.bind("<Left>", move)
root.bind("<Right>", move)

# Run the Tkinter event loop
root.mainloop()
