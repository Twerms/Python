import turtle
import random
import math
from turtle import onkeypress  
from turtle import listen 

turtle.shape("turtle")

def drawRectangle(ul, w, h):
    # move to ul
    turtle.up()
    turtle.goto(ul[0], ul[1])
    turtle.down()
    # face right
    turtle.setheading(0)
    # go forward by width
    turtle.forward(w)
    # turn right 90
    turtle.right(90)
    # go forward by height
    turtle.forward(h)
    # ...
    turtle.right(90)
    turtle.forward(w)
    turtle.right(90)
    turtle.forward(h)

# draw the bounding square (i.e., the walls)
drawRectangle((-200, 200), 400, 400)
turtle.hideturtle()

############## Paddle Stuff

# make a turtle for the paddle!
paddle = turtle.Turtle()
paddle.setheading(90)
paddle.shape('square')
paddle.fillcolor("pink")
paddle.turtlesize(1.5, 6)

paddle_x = -170
paddle_y = 0
paddle.up()
paddle.goto(paddle_x, paddle_y)

def go_up():
    global paddle_y
    paddle_y = paddle_y + 10
    # make sure we don't go past the top
    if paddle_y >= 140:
        paddle_y = 140
    paddle.goto(paddle_x, paddle_y)

def go_down():
    global paddle_y
    paddle_y = paddle_y - 10
    # make sure we don't go past the bottom
    if paddle_y <= -140:
        paddle_y = -140
    paddle.goto(paddle_x, paddle_y)

# set up functions to run every time the up/down keys are pressed
onkeypress(go_up, "Up")
onkeypress(go_down, "Down")
listen()

############## Ball Stuff
ball = turtle.Turtle()
ball.shape("square")
ball.fillcolor("pink")
ball.turtlesize(2, 2)
ball_width = 40

# we'll use these variables to keep track of where the ball
# should be/where it should move
ball_x = random.randint(0, 150) # always on the right
ball_y = random.randint(-150, 150)
# these two variables together will form our direction
ball_xoffset = random.uniform(-1.0, 1.0)
ball_yoffset = random.uniform(-1.0, 1.0)
# let's *normalize* our direction so that it has a length 1 hypotenuse
direction_hyp_length = math.sqrt(ball_xoffset**2 + ball_yoffset**2)
ball_xoffset = ball_xoffset / direction_hyp_length * 2
ball_yoffset = ball_yoffset / direction_hyp_length * 2
# now the length of the hypotenuse is 2

# put the turtle in the correct starting location
ball.up()
ball.goto(ball_x, ball_y)

def bounce_if_hit_wall():
    global ball_x
    global ball_y
    global ball_xoffset
    global ball_yoffset
    global is_game_over
    
    if ball_y <= -180:
        # we either hit the bottom wall, or we're trying to go below it
        # move the turtle back inside
        ball_y = -180
        # change the y offset so we move upwards now
        ball_yoffset = ball_yoffset * -1

    if ball_y >= 180:
        # we either hit the top wall, or we're trying to go above it
        # move the turtle back inside
        ball_y = 180
        # change the y offset so we move downwards now
        ball_yoffset = ball_yoffset * -1

    if ball_x <= -180:
        # we either hit the left wall, or we're trying to go past it
        # move the turtle back inside
        ball_x = -180
        # change the x offset so we move to the right now
        is_game_over = True

    if ball_x >= 180:
        # we either hit the right wall, or we're trying to go past it
        # move the turtle back inside
        ball_x = 180
        # change the x offset so we move to the left now
        ball_xoffset = ball_xoffset * -1

def bounce_if_hit_paddle():
    global ball_x
    global ball_xoffset
    A = ball_x <= paddle_x + 15 + 20
    B = ball_y <= paddle_y + 60 + 20
    C = ball_y >= paddle_y - 60 - 20

    if A and B and C:
        ball_x = paddle_x + 15 + 20
        ball_xoffset = ball_xoffset * -1

def drawFrame():
    global ball_x
    global ball_y
    global ball_xoffset
    global ball_yoffset
    
    # change the turtle's x coordinate by the offset
    ball_x = ball_x + ball_xoffset
    # change the turtle's y coordinate by the offset
    ball_y = ball_y + ball_yoffset

    # if we hit a wall, bounce off
    bounce_if_hit_wall() 
    
    bounce_if_hit_paddle()
    
    # redraw the turtle
    ball.goto(ball_x, ball_y)

is_game_over = False

while not is_game_over:
    drawFrame()