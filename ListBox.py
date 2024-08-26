import tkinter as tk

def add_item():
    entry_text = entry.get()
    if entry_text:
        listbox.insert(tk.END, entry_text)
        entry.delete(0, tk.END)

def remove_item():
    selected_indices = listbox.curselection()
    for index in selected_indices:
        listbox.delete(index)

# Create the main window
root = tk.Tk()
root.title("Listbox Example")
root.geometry("300x300")

# Create a frame
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Create the Listbox widget
listbox = tk.Listbox(frame, selectmode=tk.MULTIPLE)
listbox.pack(side=tk.LEFT, padx=5)

# Create a scrollbar
scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Link the Listbox with the scrollbar
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Create an Entry widget to input new items
entry = tk.Entry(root, width=20)
entry.pack(pady=5)

# Create "Add" and "Remove" buttons
add_button = tk.Button(root, text="Add", command=add_item)
add_button.pack(side=tk.LEFT, padx=5)
remove_button = tk.Button(root, text="Remove", command=remove_item)
remove_button.pack(side=tk.LEFT, padx=5)

# Run the Tkinter event loop
root.mainloop()
