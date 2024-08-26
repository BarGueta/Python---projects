import tkinter as tk
from tkinter import filedialog

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                              filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_widget.get("1.0", tk.END))

# Create the main window
root = tk.Tk()
root.title("Save File Dialog Example")

# Create a text widget for user input
text_widget = tk.Text(root, wrap=tk.WORD)
text_widget.pack(fill=tk.BOTH, expand=True)

# Create a "Save File" button
save_button = tk.Button(root, text="Save File", command=save_file)
save_button.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
