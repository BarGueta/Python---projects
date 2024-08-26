import tkinter as tk
from tkinter import messagebox

def divide():
    try:
        x = float(entry1.get())
        y = float(entry2.get())
        result = x / y
        result_label.config(text="Division result: {:.2f}".format(result))
    except ZeroDivisionError as e:
        messagebox.showerror("Error", "ZeroDivisionError: " + str(e))
    except ValueError as e:
        messagebox.showerror("Error", "ValueError: " + str(e))
    except Exception as e:
        messagebox.showerror("Error", "Exception is: " + str(e))

# Create the main application window
root = tk.Tk()
root.title("Exception Handling with Tkinter")
root.geometry("300x150")

# Create input fields
entry1_label = tk.Label(root, text="Enter first number:")
entry1_label.pack()
entry1 = tk.Entry(root)
entry1.pack()

entry2_label = tk.Label(root, text="Enter second number:")
entry2_label.pack()
entry2 = tk.Entry(root)
entry2.pack()

# Create a button to perform division
divide_button = tk.Button(root, text="Divide", command=divide)
divide_button.pack()

# Label to display result
result_label = tk.Label(root, text="")
result_label.pack()

# Run the Tkinter event loop
root.mainloop()
