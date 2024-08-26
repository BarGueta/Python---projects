import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Notebook Example")
root.geometry("300x150")
root.resizable(False, False)

# Create a Notebook widget
notebook = ttk.Notebook(root)
notebook.pack(fill=tk.BOTH, expand=True)

# Create tabs
tab1 = tk.Frame(notebook)
tab2 = tk.Frame(notebook)

notebook.add(tab1, text='Tab 1')
notebook.add(tab2, text='Tab 2')

# Add content to Tab 1
label_tab1 = tk.Label(tab1, text="This is Tab 1")
label_tab1.pack(padx=20, pady=20)

# Add content to Tab 2
label_tab2 = tk.Label(tab2, text="This is Tab 2")
label_tab2.pack(padx=20, pady=20)

# Run the Tkinter event loop
root.mainloop()
