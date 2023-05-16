import turtle
import random

number = int(turtle.textinput("Number of Shapes", "How many shapes would you like?"))

pen = turtle.Turtle()

shapes = 0
while shapes < number:
    color = random.choice(["red", "orange", "yellow", "green", "blue", "purple", "pink"])
    shape = random.choice(["square", "triangle"])
    
    size = random.randint(20, 100)
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)

    pen.color(color)
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    
    if shape == "square":
        for i in range(4):
            pen.forward(size)
            pen.right(90)
    elif shape == "triangle":
        for i in range(3):
            pen.forward(size)
            pen.left(120)
            
    shapes += 1
    
pen.hideturtle()
turtle.exitonclick()
