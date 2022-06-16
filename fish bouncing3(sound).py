import turtle
#import winsound
import time
wn=turtle.Screen()
wn.setup(600,600)
def AQUARIUM(AQ):
    wn.bgpic(AQ)
image1 = ("Fish3.gif")
image2 = ("Fish1.gif")
imageaq1=('aq1.gif')
imageaq2=('aq2.gif')
imageaq3=('aq3.gif')
imageaq4=('aq4.gif')
imageaq5=('aq5.gif')
AQ=[imageaq1,imageaq2,imageaq3,imageaq4,imageaq5]
t=turtle.Turtle()
t.showturtle()
t.speed(10)
t.penup()
X=-90
Y=-90
dx=2
dy=1
import winsound
winsound.PlaySound('music2.wav', winsound.SND_ASYNC)

def motion(image):
    wn.addshape(image)
    t.shape(image)
    t.showturtle()
motion(image1)    
k=0
while True:
    k=k+1
    k1=k%5
    t.setx(X+dx)
    t.sety(Y+dy)
    X=t.xcor()
    Y=t.ycor()
    AQUARIUM(AQ[k1])
    if X<-160:
        motion(image1)
        dx=-dx  
    if X>150:
        motion(image2)
        dx=-dx  
    if Y<-105:
        dy=-dy  
    if Y>110:
        dy=-dy
    

        

