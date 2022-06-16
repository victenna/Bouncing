import turtle,random,time
wn=turtle.Screen()
wn.bgcolor('gold')
turtle.tracer(2)
border=turtle.Turtle()
border.hideturtle()
border.speed(0)
border.pensize(2)
border.up()
border.goto(-250,250)
border.down()
border.goto(-250,-250)
border.goto(250,-250)
border.goto(250,250)

balls=[]
clr=['green','blue','yellow','violet','red']
for i in range(5):
    balls.append(turtle.Turtle('circle'))
    balls[i].color(clr[i])
    balls[i].up()
    balls[i].goto(random.randint(-200,200),250)
         

gravity=0.2
dy=2
dx=[-3,5,1,-2,4]
while True:
    time.sleep(0.01)
    for q in range (5):
        
        X=int(balls[q].xcor()+dx[q])
        Y=int(balls[q].ycor()-dy)
        balls[q].goto(X,Y)
        dy=round((dy+gravity),1)
        
        if Y<=-230:
            dy=-dy

        if X>=240 or X<=-240:
            dx[q]=-dx[q]
