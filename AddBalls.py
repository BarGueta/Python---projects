#Add balls and reset:
from tkinter import *
import time
import random

class Ball:

    def __init__(self,canvas,x,y,diameter,xVelocity,yVelocity,color):
        self.canvas = canvas
        self.image = canvas.create_oval(x,y,diameter,diameter,fill=color)
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity

    def move(self):
        coordinates = self.canvas.coords(self.image)

        if(coordinates[2]>=(self.canvas.winfo_width()) or coordinates[0]<0):
            self.xVelocity = -self.xVelocity
        if(coordinates[3]>=(self.canvas.winfo_height()) or coordinates[1]<0):
            self.yVelocity = -self.yVelocity

        self.canvas.move(self.image,self.xVelocity,self.yVelocity)
#---------------------------------------
window = Tk()
window.title("Multiple balls animations")
window.resizable(False,False)

ballist = []
ballcount = 0

def addball():
    global ballcount
    colorlist = ["red", "green", "yellow", "orange", "white"]
    randomcolor = random.choice(colorlist)
    randomdiameter = random.randint(50, 125)
    randomyvelocity = random.randint(3, 7)
    randomxvelocity = random.randint(3, 7)
    createdball = "basket_ball"+str(ballcount)
    createdball = Ball(canvas, 0, 0, randomdiameter, randomxvelocity, randomyvelocity, randomcolor)
    ballcount +=1
    ballist.append(createdball)

def vanishallballs():
    global ballist
    ballist = []
    canvas.delete('all')

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

createbutton = Button(window,text="Click to create a ball",command=addball)
createbutton.pack()

resetbutton = Button(window,text="Click to Reset",command=vanishallballs)
resetbutton.pack()

while True:
    for i in ballist:
        i.move()
    window.update()
    time.sleep(0.01)

window.mainloop()