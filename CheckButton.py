import tkinter as tk

def check_button_callback():
    if check_var.get() == 1:
        print("Check button is selected")
        info_label.config(text="Check button is selected")
    else:
        print("Check button is not selected")
        info_label.config(text="Check button is not selected")

# Create the main window
root = tk.Tk()
root.geometry("300x150")
root.title("Check Button Example")

# Create a variable to hold the state of the check button
check_var = tk.IntVar()

# Create the check button
check_button = tk.Checkbutton(root, text="Check Button", variable=check_var, command=check_button_callback)
check_button.pack(pady=10)

info_label = tk.Label(text="Check button is not selected")
info_label.place(relx=0.5, rely=0.5, anchor="center")

# Run the Tkinter event loop
root.mainloop()
