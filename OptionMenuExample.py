from tkinter import *

#A function that can be used for the command besides the lambda choice... (command = choice)
def choice(selected):
    print("User selected:",selected)

root = Tk()
root.geometry("400x100")
root.title("Option menu example")
root.resizable(False,False)

# Create a list of options
options = ["Option 1", "Option 2", "Option 3", "Option 4"]

# Create a variable to store the selected option
selected_option = StringVar(root)
selected_option.set(options[0])  # Set the default option

# Create the OptionMenu widget
option_menu = OptionMenu(root, selected_option, *options, command = lambda choice: print("User selected:",selected_option.get()))
option_menu.pack()

root.mainloop()