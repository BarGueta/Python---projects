from tkinter import *

# label = an area widget that holds text and/or an image within a window

window = Tk()

photo = PhotoImage(file="AnimatedBeach.png")  # The entire file path is not required when a file is on the project folder - the folder with the Python file that we are working with

# Creating a label object.
#Arguments: the name of the container(window) and options.Options are keyword arguments that can be passed in to the constructor.The constructor is a method that is called when an object is created of a class

label = Label(window,
             text="This is a PhotoImage:",
             font=('Arial', 40, 'bold'),
             fg='#00FF00',
             bg='black',
             relief=RAISED,
             bd=10,
             padx=20,
             pady=20,
             image=photo,
             compound='bottom')


# bg = background color , fg = foreground color , relief = border style , bd = border width , padx = space between the border and the text from left and right , pady = space between the border above and below the text, compound = set a direction of where the image will be placed relative to the text


label.pack()  # adds the label to the window. The label will be placed in the top center of the window
# label.place(x=0,y=0) #another way to add a widget and also set coordinates with x and y options

window.mainloop()
