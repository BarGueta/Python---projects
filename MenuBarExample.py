import tkinter as tk

#Every cascade has a command that needs to be written...
def file_new():
    print("New File")

def file_open():
    print("Open File")

def file_save():
    print("Save File")

def file_save_as():
    print("Save File As")

def edit_cut():
    print("Cut")

def edit_copy():
    print("Copy")

def edit_paste():
    print("Paste")

# Create the main window
root = tk.Tk()
root.title("Menu Bar Example")
root.geometry("300x300")

# Create a menu bar
menubar = tk.Menu(root)
root.config(menu=menubar)

# Create File menu
file_menu = tk.Menu(menubar, tearoff=False)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=file_new)
file_menu.add_command(label="Open", command=file_open)
file_menu.add_separator()
file_menu.add_command(label="Save", command=file_save)
file_menu.add_command(label="Save As", command=file_save_as)

# Create Edit menu
edit_menu = tk.Menu(menubar, tearoff=False)
menubar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=edit_cut)
edit_menu.add_command(label="Copy", command=edit_copy)
edit_menu.add_command(label="Paste", command=edit_paste)

# Run the Tkinter event loop
root.mainloop()
