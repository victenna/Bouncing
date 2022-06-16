import turtle
turtle.bgcolor('gold')
t=turtle.Turtle('circle')
t1=turtle.Turtle()
t.turtlesize(2)
t.hideturtle()
t.color('red')
t.penup()
t1.hideturtle()
t1.pensize(20)
t1.penup()
t1.goto(-200,200)
t1.pendown()
t1.color('blue')
for m in range(4):
    t1.fd(400)
    t1.right(90)
t.goto(100,100)
dx=1.3
dy=2.3
X=50
Y=50
t.speed('fastest')
t.showturtle()
while True:
    t.goto(X+dx,Y+dy)
    X=t.xcor()
    Y=t.ycor()         
    if X<-175:
        dx=dx*-1              
    if X>175:
        dx=dx*-1        
    if Y<-175:
        dy=dy*-1
    if Y>175:
        dy=dy*-1
