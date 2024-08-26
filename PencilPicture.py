import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


def pencil_sketch(image_path):
    global original_photo
    global pencil_sketch_label

    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Invert the grayscale image
    inverted_gray_image = 255 - gray_image

    # Blur the inverted image using GaussianBlur
    blurred_image = cv2.GaussianBlur(inverted_gray_image, (21, 21), 0)

    # Invert the blurred image
    inverted_blurred_image = 255 - blurred_image

    # Create the pencil sketch image by dividing the grayscale image by the inverted blurred image
    pencil_sketch_image = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)

    # Convert OpenCV BGR image to RGB and then to PIL Image
    pencil_sketch_image = cv2.cvtColor(pencil_sketch_image, cv2.COLOR_GRAY2RGB)
    pencil_sketch_image = Image.fromarray(pencil_sketch_image)

    # Convert PIL Image to Tkinter PhotoImage
    pencil_sketch_photo = ImageTk.PhotoImage(pencil_sketch_image)

    # Display the original image and the pencil sketch image
    original_label.config(image=original_photo)
    original_label.image = original_photo
    pencil_sketch_label.config(image=pencil_sketch_photo)
    pencil_sketch_label.image = pencil_sketch_photo


def open_image():
    global original_photo

    # Open file dialog to select an image
    file_path = filedialog.askopenfilename()

    # Convert the selected image to PIL Image and resize if needed
    original_image = Image.open(file_path)
    original_image.thumbnail((400, 400))

    # Convert PIL Image to Tkinter PhotoImage
    original_photo = ImageTk.PhotoImage(original_image)

    # Call the pencil_sketch function with the selected image path
    pencil_sketch(file_path)


# Create the main window
root = tk.Tk()
root.title("Pencil Sketch App")

# Create a button to open an image
open_button = tk.Button(root, text="Open Image", command=open_image, width=40)
open_button.pack(pady=10)

# Create labels to display the original image and the pencil sketch image
original_label = tk.Label(root)
original_label.pack(side=tk.LEFT, padx=10)
pencil_sketch_label = tk.Label(root)
pencil_sketch_label.pack(side=tk.RIGHT, padx=10)

# Start the GUI
root.mainloop()
