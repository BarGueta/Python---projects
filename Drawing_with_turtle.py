import turtle
import random

# Create a turtle screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")

# Create a turtle
pen = turtle.Turtle()
pen.speed(0)
pen.width(2)

# Function to draw a colorful star
def draw_star(size):
    pen.begin_fill()
    for _ in range(5):
        pen.forward(size)
        pen.right(144)
    pen.end_fill()

# Draw multiple stars at random positions
for _ in range(30):
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    pen.penup()
    pen.goto(x, y)
    pen.color(random.random(), random.random(), random.random())  # Random RGB color
    pen.pendown()
    draw_star(random.randint(10, 50))

# Hide the turtle
pen.hideturtle()

# Keep the window open
screen.mainloop()
