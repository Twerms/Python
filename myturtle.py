import turtle

turtle.setup(width=600, height=400)
turtle.title("Name Initials and Graduation Year")
draw = turtle.Turtle()

# Color and size
draw.pencolor("blue")
draw.pensize(5)

# Position first
draw.penup()
draw.right(180)
draw.forward(125)
draw.pendown()

# F
draw.right(90)
draw.forward(100)
draw.right(90)
draw.forward(50)
draw.right(180)
draw.forward(50)
draw.left(90)
draw.forward(50)
draw.left(90)
draw.forward(50)

# Reposition
draw.penup()
draw.forward(25)
draw.left(90)
draw.pendown()

# B
draw.forward(50)
draw.right(180)
draw.forward(100)
draw.left(90)
draw.forward(50)
draw.left(90)
draw.forward(50)
draw.left(90)
draw.forward(50)
draw.left(180)
draw.forward(50)
draw.left(90)
draw.forward(50)
draw.left(90)
draw.forward(50)

# Reposition
draw.penup()
draw.right(180)
draw.forward(75)
draw.pendown()

# 2
draw.forward(50)
draw.right(90)
draw.forward(50)
draw.right(90)
draw.forward(50)
draw.left(90)
draw.forward(50)
draw.left(90)
draw.forward(50)

# Reposition
draw.penup()
draw.forward(25)
draw.pendown()

# 6
draw.left(90)
draw.forward(100)
draw.right(90)
draw.forward(50)
draw.left(180)
draw.forward(50)
draw.left(90)
draw.forward(50)
draw.left(90)
draw.forward(50)
draw.right(90)
draw.forward(50)
draw.right(90)
draw.forward(50)


draw.hideturtle()
turtle.done()