from tkinter import *

# Toplevel() = When closing the bottom window, the top window will close itself as well

def create_window():
   new_window = Toplevel()
   new_window.geometry("250x250")


old_window = Tk()
old_window.geometry("300x150")


Button(old_window, text="create new window", command=create_window).pack()


old_window.mainloop()
