# Color chooser:
from tkinter import *
from tkinter import colorchooser

# Will change the background color of the window according to the chosen color
def click():
   color = colorchooser.askcolor()
   print(color)  # will print RGB values as the first element and the second one is the hexadecimal representation of the RGB values
   print(type(color))  # colorchooser.askcolor() is a tuple…
   colorHex = color[1]  # The second element from the tuple that is stored in the color variable - the hex value
   window.config(bg=colorHex)  # Change background color


window = Tk()
window.geometry("420x420")
button = Button(text='click me', command=click)
button.pack()
window.mainloop()
