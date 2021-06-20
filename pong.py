import turtle

wn = turtle.Screen()
wn.title("Pong with turtles")
wn.bgcolor("black")
wn.setup(800, 600)
wn.tracer(0)


# Score
score_a = 0
score_b = 0

# Paddle 1
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)
paddle_a.is_ai = True

# Paddle 2
paddle_b = turtle.Turtle()
paddle_b.speed(1)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid = 5,stretch_len = 1)
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.is_ai = True

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dSpeed = 0.15
ball.dx = ball.dSpeed
ball.dy = ball.dSpeed


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: %d  |  Player 2 = %d" %(score_a, score_b), align="center", font=("Courier", 18,"normal"))



# Moviment Functions
def paddle_a_up():
    paddle_a.sety(paddle_a.ycor() + 20)

def paddle_a_down():
    paddle_a.sety(paddle_a.ycor() - 20)

def paddle_b_up():
    paddle_b.sety(paddle_b.ycor() + 20)

def paddle_b_down():
    paddle_b.sety(paddle_b.ycor() - 20)



# Keyboard

wn.listen()


if not paddle_a.is_ai: 
    wn.onkeypress(paddle_a_up,   "w")
    wn.onkeypress(paddle_a_down, "s")

if not paddle_b.is_ai: 
    wn.onkeypress(paddle_b_up,   "Up")
    wn.onkeypress(paddle_b_down, "Down")

while True:
    wn.update()

    # Paddle A AI
    if paddle_a.is_ai:
        if paddle_a.ycor() != ball.ycor():
            if ball.ycor() > paddle_a.ycor():
                paddle_a.sety(paddle_a.ycor() + 0.1)
            else:
                paddle_a.sety(paddle_a.ycor() - 0.1)

    # Paddle B AI
    if paddle_b.is_ai:
        if paddle_b.ycor() != ball.ycor():
            if ball.ycor() > paddle_b.ycor():
                paddle_b.sety(paddle_b.ycor() + 0.1)
            else:
                paddle_b.sety(paddle_b.ycor() - 0.1)


    # Move Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border cheking
    #  Y
    if ball.ycor() >  290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1
    #  X
    if ball.xcor() >  380:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player 1: %d  |  Player 2 = %d" %(score_a, score_b), align="center", font=("Courier", 18,"normal"))
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player 1: %d  |  Player 2 = %d" %(score_a, score_b), align="center", font=("Courier", 18,"normal"))

    # Paddle A Collision w/ Ball
    if     ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor()-50:
        if ball.xcor() < paddle_a.xcor() + 15 and ball.xcor() > paddle_a.xcor()-10:
            ball.dx *= -1
    # Paddle B Collision w/ Ball
    if     ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor()-50:
        if ball.xcor() < paddle_b.xcor() + 15 and ball.xcor() > paddle_b.xcor()-10:
            ball.dx *= -1
