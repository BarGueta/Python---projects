import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename(initialdir="C:\\Users\\User\\PycharmProjects\\Projects for YT shorts",
                                           title="Choose a text file",
                                           filetypes=(("Text files", "*.txt"),("all files","*.*")))
    if file_path:
        with open(file_path, 'r') as file:
            file_contents = file.read()
            text_widget.insert(tk.END, file_contents)

# Create the main window
root = tk.Tk()
root.title("File Dialog Example")

# Create a text widget to display file contents
text_widget = tk.Text(root, wrap=tk.WORD)
text_widget.pack(fill=tk.BOTH, expand=True)

# Create an "Open File" button
open_button = tk.Button(root, text="Open File", command=open_file)
open_button.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
