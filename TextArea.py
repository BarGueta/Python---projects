from tkinter import *

def Text_area_callback():
   input = text.get("1.0",END) # get all the lines ("1.0" is the beginning index - first line and in order to get everything the second index is END)
   print("Yow wrote:")
   print(input)


window = Tk()
window.title("Text area")
window.resizable(False, False)
text = Text(window,
           font=("Arial", 25),
           height=8,
           width=20,
           padx=20,
           pady=20)
text.pack()
button = Button(window, text="submit", command=Text_area_callback)
button.pack()
window.mainloop()
