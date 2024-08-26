from tkinter import *

# New independent window

def create_window():
   new_window = Tk()
   new_window.geometry("250x250")


old_window = Tk()
old_window.geometry("300x150")


Button(old_window, text="create new window", command=create_window).pack()


old_window.mainloop()
