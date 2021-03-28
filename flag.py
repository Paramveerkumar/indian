#import the necessary module
import turtle
flag=turtle.Turtle()
flag.pensize(5)
flag.speed(3)

def move(x,y):
    flag.penup()
    flag.goto(x,y)
    flag.pendown()
#Ashok Chakra
flag.color("#054187")
for i in range(24):
    flag.forward(80);
    flag.backward(80);
    flag.left(15)
move(0,-80)
flag.circle(80,360)

#Green Rectangle
flag.begin_fill()
flag.color("green")
flag.forward(350)
flag.backward(700)
flag.right(90)
flag.forward(200)
flag.left(90)
flag.forward(700)
flag.left(90)
flag.forward(200)
flag.left(90)
flag.end_fill()
#0range rectangle
flag.color("orange")
move(-350,80)
flag.begin_fill()
flag.right(180)
flag.forward(700)
flag.left(90)
flag.forward(200)
flag.left(90)
flag.forward(700)
flag.left(90)
flag.forward(200)
flag.end_fill()





