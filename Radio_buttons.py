from tkinter import *

#in radio buttons, just one can be selected from a group

button_list = ["Radio button 1", "Radio button 2", "Radio button 3"]

def Click():
   if (x.get() == 0):
       print("You clicked radio button 1")
   elif (x.get() == 1):
       print("You clicked radio button 2")
   elif (x.get() == 2):
       print("You clicked radio button 3")
   else:
       print("huh?")


window = Tk()
window.title("Radio buttons")

x = IntVar()


for index in range(len(button_list)):  # creating a radio button for each item in the list with a for loop with the length of the list
   radiobutton = Radiobutton(window,
                             text=button_list[index],  # adds text to radio buttons
                             variable=x,  # groups radiobuttons together if they share the same variable
                             value=index,  # assigns each radiobutton a different value
                             padx=25,  # adds padding on x-axis
                             compound='left',  # adds image & text (left-side)
                             command=Click,  # set command of radiobutton to function
                             font=('Arial',25)
                             )
   radiobutton.pack(anchor=W)  # anchor radio buttons to the west side


window.mainloop()
