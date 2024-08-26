import tkinter as tk

class DraggableLabel(tk.Label):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.bind("<Button-1>", self.on_drag_start)
        self.bind("<B1-Motion>", self.on_drag_motion)
        self.bind("<ButtonRelease-1>", self.on_drag_release)
        self.dragging = False

    def on_drag_start(self, event):
        self.dragging = True
        self.start_x = event.x
        self.start_y = event.y

    def on_drag_motion(self, event):
        if self.dragging:
            x = self.winfo_x() - self.start_x + event.x
            y = self.winfo_y() - self.start_y + event.y
            self.place(x=x, y=y)

    def on_drag_release(self, event):
        self.dragging = False

# Create the main application window
root = tk.Tk()
root.title("Draggable Label Example")
root.geometry("600x600")
root.resizable(False, False)

# Create a draggable label
label = DraggableLabel(root, text="Drag me!", bg="lightblue", relief="raised", width=20,height=5)
label.place(x=50, y=50)

# Run the Tkinter event loop
root.mainloop()
