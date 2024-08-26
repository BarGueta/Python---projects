#Ping pong game - maybe improve later:
from tkinter import *
from pygame import error
from pygame import mixer
import time
#----------------------------------------------------------
#Initial values for variables:
mixer.init()
WIDTH = 900
HEIGHT = 500
p1score,p2score = 0,0
xvelocity,yvelocity = -5,-5
#----------------------------------------------------------
def firstgame():
 playfirst.destroy()
 game()
#----------------------------------------------------------
def game():
 global p1score,p2score,gameover,restartbutton
 restartbutton.destroy()
 gameover.destroy()
 p1score,p2score = 0,0
 scorelabel.config(text=str(p1score) + ":" + str(p2score))
 while p1score < 5 and p2score < 5:
    move()
    window.update()
    time.sleep(0.01)
 gameover = Label(window, text="Game over!", bg="black", fg="white", font=('Arial', 20))
 gameover.place(relx=0.5,rely=0.75,anchor="center")
 restartbutton = Button(window, text="Play again", bg="black", fg="white", font=('Arial', 15),command=game)
 restartbutton.place(relx=0.5,rely=0.85,anchor="center")
#----------------------------------------------------------
def move():
   global allscore, p1score, p2score, xvelocity, yvelocity
   p1coords = canvas.coords(p1)
   p2coords = canvas.coords(p2)
   ballcoords = canvas.coords(ball)

   overlappingitems1 = canvas.find_overlapping(p1coords[0],p1coords[1],p1coords[2],p1coords[3])
   overlappingitems2 = canvas.find_overlapping(p2coords[0],p2coords[1],p2coords[2],p2coords[3])
   # ------------------------------------------------
   if ball in overlappingitems1:
       beep()
       canvas.move(ball,7,0) #maybe change the x move
       xvelocity = -xvelocity

   if ball in overlappingitems2:
       beep()
       canvas.move(ball,-7,0) #maybe change the x move
       xvelocity = -xvelocity
   # ------------------------------------------------
   if (ballcoords[2] >= WIDTH):
       p1score += 1
       scorelabel.config(text = str(p1score)+":"+str(p2score))
       canvas.move(ball,-(WIDTH/2),0)
   # ------------------------------------------------
   if(ballcoords[0] <= 0):
       p2score += 1
       scorelabel.config(text = str(p1score)+":"+str(p2score))
       canvas.move(ball, WIDTH/2, 0)
   # ------------------------------------------------
   if (ballcoords[3] >= (HEIGHT) or ballcoords[1] < 0):
       yvelocity = -yvelocity

   canvas.move(ball,xvelocity,yvelocity)
#----------------------------------------------------------
def beep():
    try:
        mixer.music.load("C:\\Users\\User\\PycharmProjects\\helloworld\\Beep.mp3")  # download a mp3 file and insert its path here...
        mixer.music.play()
    except error as e:
        print(f"file not found: {str(e)}")
#----------------------------------------------------------
def moveupp1(event):
   p1coords = canvas.coords(p1)
   if (p1coords[1] <= 0):
       pass
   else:
       canvas.move(p1, 0, -100)
#----------------------------------------------------------
def movedownp1(event):
   p1coords = canvas.coords(p1)
   if (p1coords[3] >= HEIGHT):
       pass
   else:
       canvas.move(p1, 0, 100)
#----------------------------------------------------------
def moveupp2(event):
   p2coords = canvas.coords(p2)
   if (p2coords[1] <= 0):
       pass
   else:
       canvas.move(p2, 0, -100)
#----------------------------------------------------------
def movedownp2(event):
   p2coords = canvas.coords(p2)
   if (p2coords[3] >= HEIGHT):
       pass
   else:
       canvas.move(p2, 0, 100)
#----------------------------------------------------------
#Basic window settings:
window = Tk()
window.title("Ping Pong")
window.resizable(False,False)
try:
    icon = PhotoImage(file="C:\\Users\\User\\PycharmProjects\\helloworld\\PongPng.png")  # give an icon to the window
    window.iconphoto(True, icon)
except:
    print("Something went wrong with photoimage...")
#----------------------------------------------------------
#Creating the canvas:
canvas = Canvas(window,width=WIDTH,height=HEIGHT,bg="black")
canvas.pack()
#----------------------------------------------------------
#Creating players, ball and other shapes:
#oval1 = canvas.create_oval(WIDTH/2-75,175,WIDTH/2+75,325,fill="white")
#oval2 = canvas.create_oval(WIDTH/2-71,179,WIDTH/2+71,321,fill="black")
line = canvas.create_line(WIDTH/2,0,WIDTH/2,HEIGHT,fill="white",width=3)
scorelabel = Label(window,text=str(p1score)+":"+str(p2score),bg="black",fg="white",font=('Arial',20))
scorelabel.place(relx=0.5,rely=0.042,anchor="center") #top middle placing...
restartbutton = Button(window)
gameover = Label(window)

playfirst = Button(window,text="Play",bg="black", fg="white", font=('Arial', 20),command=firstgame)
playfirst.place(relx=0.5,rely=0.85,anchor="center")

p1 = canvas.create_rectangle(70, 200, 80, 300, fill="red")
p2 = canvas.create_rectangle(820, 200, 830, 300, fill="blue")
ball = canvas.create_oval(WIDTH/2-10,HEIGHT/2-10,WIDTH/2+10,HEIGHT/2+10, fill="white")

#----------------------------------------------------------
#Binding:
window.bind("<w>",moveupp1)
window.bind("<s>",movedownp1)
window.bind("<Up>",moveupp2)
window.bind("<Down>",movedownp2)
#----------------------------------------------------------
window.mainloop()
#----------------------------------------------------------