#MovingCar:
#Import modules
from tkinter import *
import tkinter as tk
import pygame
from pygame import mixer
from time import strftime
import time

#general settings
xVelocity = 1
yVelocity = 1
WIDTH = 618
HEIGHT = 347
mixer.init()
root = tk.Tk()
canvas = Canvas(root,width=WIDTH,height=HEIGHT)
canvas.pack()
root.title("Chilling car")
root.resizable(False,False)
icon = PhotoImage(file="AnimatedBeach.png") #give an icon to the window
root.iconphoto(True,icon)

#creating functions:

def timee():
    string = strftime('%H:%M:%S %p')
    clock.config(text=string)
    clock.after(1000, timee)

clock = Label(canvas,fg='black', bg='white',font='DS-Digital')
clock.place(x = 280, y = 0)
timee()

basad = Label(canvas,fg='black', bg='white',text='בס"ד')
basad.place(x = 588, y = 0 )

#Creating Amination:

background_photo = PhotoImage(file='AnimatedBeach.png')
background = canvas.create_image(0,0,image=background_photo,anchor=NW)

photo_image = PhotoImage(file='sbitcar-removebg-preview.png')
my_image = canvas.create_image(0,260,image=photo_image,anchor=NW)

image_width = photo_image.width()
image_height = photo_image.height()

while True:
    coordinates = canvas.coords(my_image)
    #print(coordinates)
    if(coordinates[0]>=(WIDTH-image_width+130) or coordinates[0]<0):
        canvas.delete(my_image)
        my_image = canvas.create_image(0, 260, image=photo_image, anchor=NW)

    canvas.move(my_image,xVelocity,0)
    root.update()
    time.sleep(0.005)

#Execute tkinter
root.mainloop()