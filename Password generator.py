import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    length = int(entry_length.get())
    include_numbers = var_include_numbers.get()
    include_special_chars = var_include_special_chars.get()

    characters = string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    if length > 0:
        password = ''.join(random.choice(characters) for _ in range(length))
        entry_generated_password.delete(0, tk.END)
        entry_generated_password.insert(tk.END, password)
    else:
        messagebox.showwarning("Warning", "Please enter a valid password length.")

root = tk.Tk()
root.title("Password Generator")
root.resizable(False, False)

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

label_length = tk.Label(frame, text="Password Length:")
label_length.grid(row=0, column=0)

entry_length = tk.Entry(frame, width=10)
entry_length.grid(row=0, column=1)

var_include_numbers = tk.BooleanVar()
check_include_numbers = tk.Checkbutton(frame, text="Include Numbers", variable=var_include_numbers)
check_include_numbers.grid(row=1, column=0, columnspan=2)

var_include_special_chars = tk.BooleanVar()
check_include_special_chars = tk.Checkbutton(frame, text="Include Special Characters", variable=var_include_special_chars)
check_include_special_chars.grid(row=2, column=0, columnspan=2)

button_generate_password = tk.Button(frame, text="Generate Password", command=generate_password)
button_generate_password.grid(row=3, column=0, columnspan=2, pady=10)

label_generated_password = tk.Label(frame, text="Generated Password:")
label_generated_password.grid(row=4, column=0, sticky="e")

entry_generated_password = tk.Entry(frame, width=30)
entry_generated_password.grid(row=4, column=1, sticky="w")

root.mainloop()
