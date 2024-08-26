from tkinter import *

# button = you click it, then it does stuff

count = 0

def click():
   global count  # access to the global variable (count)
   count += 1
   print("You clicked " + str(count) + " times")
   label.config(text="You clicked " + str(count) + " times")


window = Tk()
window.title("Click Counter")
window.geometry("420x200")

button = Button(window,
               text="click me!",
               command=click,
               font=("Comic Sans", 30),
               fg="#00FF00",
               bg="black",
               activeforeground="#00FF00",
               activebackground="black",
               state=ACTIVE,
               compound='bottom')

button.pack()

label = Label(fg="#00FF00",
             bg="black",
             font=("Comic Sans", 30),
             text="You clicked " + str(count) + " times",
             padx=25,
             pady=25)

label.pack()

window.config(background="black")

window.mainloop()
