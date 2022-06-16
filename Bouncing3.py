import turtle,random,time
border=turtle.Turtle()
border.hideturtle()
border.speed(0)
border.pensize(5)
border.up()
border.goto(-250,250)
border.down()
border.goto(-250,-250)
border.goto(250,-250)
border.goto(250,250)
ball=turtle.Turtle('circle')
ball.color('blue')
ball.shapesize(1)
ball.up()
ball.goto(0,200)
ball.speed(10)
wn=turtle.Screen()
wn.bgcolor('yellow')
X=-125
Y=250
dx=1
dy=2
gravity=0.2

while True:
    ball.goto(X,Y)
    X=int(ball.xcor()+dx)
    Y=int(ball.ycor()-dy)
    dy=(round((dy+gravity),1))
    if Y<-239:
        #print(dy)
        dy=-1*dy
    if X>240 or X<-240 :
        dx=-1*dx
