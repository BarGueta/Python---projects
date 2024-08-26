import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
import os

class ImageViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Viewer")
        self.root.geometry("700x700")
        self.root.resizable(False, False)

        self.button_frame = tk.Frame()
        self.button_frame.pack()

        self.previous = tk.Button(self.button_frame, text="previous", command=self.previous_image)
        self.previous.grid(row=0,column=0)

        self.load_button = tk.Button(self.button_frame, text="Select directory", command=self.load_images)
        self.load_button.grid(row=0,column=1)

        self.next = tk.Button(self.button_frame, text="next", command=self.next_image)
        self.next.grid(row=0,column=2)

        self.canvas = tk.Canvas(root)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.image_files = []
        self.current_image_index = 0

    def load_images(self):
        global directory
        directory = filedialog.askdirectory()
        if directory:
            self.image_files = [f for f in os.listdir(directory) if f.endswith(('.png', '.jpg', '.jpeg', '.gif'))]
            if self.image_files:
                self.show_image()

    def show_image(self):
        if self.image_files:
            image_path = os.path.join(directory, self.image_files[self.current_image_index])
            image = Image.open(image_path)

            # Calculate the aspect ratio of the image
            width_ratio = self.canvas.winfo_width() / image.width
            height_ratio = self.canvas.winfo_height() / image.height
            ratio = min(width_ratio, height_ratio)

            # Resize the image to fit the canvas while maintaining aspect ratio
            new_width = int(image.width * ratio)
            new_height = int(image.height * ratio)
            image = image.resize((new_width, new_height))

            photo = ImageTk.PhotoImage(image)

            # Clear previous image
            self.canvas.delete("all")

            # Display the image on the canvas
            self.canvas.create_image(self.canvas.winfo_width() / 2, self.canvas.winfo_height() / 2, image=photo,
                                     anchor=tk.CENTER)

            # Keep a reference to the image to prevent it from being garbage collected
            self.canvas.image = photo

    def next_image(self):
        self.current_image_index = (self.current_image_index + 1) % len(self.image_files)
        self.show_image()

    def previous_image(self):
        self.current_image_index = (self.current_image_index - 1) % len(self.image_files)
        self.show_image()

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageViewer(root)
    root.mainloop()
