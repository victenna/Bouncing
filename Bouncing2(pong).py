import turtle
wn= turtle.Screen()
wn.bgcolor("black")
wn.title("Pong")
wn.tracer(5)
#Score
score1=0
FONT = ("Arial", 44, "normal")
s1 = turtle.Turtle()
s1.hideturtle()
#s1 = turtle.Turtle(visible=False)
s1.speed("fastest")
s1.color("white")
s1.penup()
s1.setposition(0,300)
s1.write(score1, font=FONT)
# set up border dimensions
border = turtle.Turtle()
border.color("white")
border.penup()
border.setposition(-300,-300)
border.pendown()
border.pensize(3)
for side in range(4):
    border.fd(600)
    border.lt(90)
border.hideturtle()
FONT = ("Arial", 44, "normal")
#create the player turtle
pr1 = turtle.Turtle()
pr1.color("white")
pr1.shape("square")
pr1.shapesize(1,3)
pr1.penup()
pr1.speed(0)
pr1.setposition(-200,-230)
pr1.setheading(90)

#Move pr1 up and down
def move1_up():
    y = pr1.ycor()
    y =y+40
    pr1.sety(y)
    if y > 200:
        pr1.goto(-200,280)
def move1_down():
    y = pr1.ycor()
    y =y-40
    pr1.sety(y)
    if y < -200:
        pr1.goto(-200,-280)
#keyboard bindings
turtle.listen()
turtle.onkey(move1_up, "Up")
turtle.onkey(move1_down, "Down")
#create the ball
ball = turtle.Turtle()
ball.color("red")
ball.shape("circle")
ball.shapesize(1.5)
ball.penup()
ball.speed(10)
ball.setposition(0,0)
#pongspeed = 5
X=0
Y=0
pdx = 15
pdy =10
def move():
    wn.update()
    global X,Y,pdx,pdy,score1
    turtle.delay(8)
    ball.setx(X+pdx)
    ball.sety(Y+pdy)
    X=ball.xcor()
    Y=ball.ycor()
    Xpr1=pr1.xcor()
    Ypr1=pr1.ycor()
    deltaX1=abs(Xpr1-X)
    deltaY1=abs(Ypr1-Y)
    if deltaX1<18 and deltaY1<40:
        if X>-200:
            score1 += 1
            s1.undo()
            s1.write(score1, font=FONT)
        pdx=-pdx
    if X<-290:
        score1=score1-1
        s1.undo()
        s1.write(score1, font=FONT)
        pdx=-pdx  
    if X>290:
        pdx=-pdx  
    if Y<-290:
        pdy=-pdy  
    if Y>290:
        pdy=-pdy
    turtle.ontimer(move,5)
turtle.ontimer(move,5)
