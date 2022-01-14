#The Malaysian flag
from turtle import *

speed(0)
penup()
goto(-250,200)
pendown()
        
def square(length):
    for n in range(2):
        begin_fill()
        color("#000080")
        forward(length)
        right(90)
        forward(length)
        right(90)
        end_fill()
square(150)

def base_of_the_flag(length,height):
    for n in range(2):
        forward(length)
        right(90)
        forward(height)
        right(90)
base_of_the_flag(450,256)

def stripes1(length, height):
    penup()
    forward(150)
    pendown()
    for n in range(5):
        global stripe_color
        stripe_color = color("#e60000")
        begin_fill()
        forward(length)
        right(90)
        forward(height)
        right(90)
        forward(length)
        penup()
        left(90)
        forward(height)
        left(90)
        pendown()
        end_fill()
stripes1(300,15)

def stripes2(lenght, height):
    stripe_color
    begin_fill()
    forward(300)
    right(90)
    forward(15)
    right(90)
    forward(450)
    right(90)
    forward(15)
    end_fill()
    penup()
    backward(30)
    right(90)
    pendown()
    for n in range(3):
        stripe_color
        begin_fill()
        forward(lenght)
        right(90)
        forward(height)
        right(90)
        forward(lenght)
        penup()
        left(90)
        forward(height)
        left(90)
        pendown()
        end_fill()
stripes2(450,15)

def CrescentAndStar():
    penup()
    left(90)
    forward(150)
    pendown()
    right(90)
    penup()
    forward(70)
    pendown()
    color("yellow")
    begin_fill()
    circle(50)
    end_fill()
    forward(25)
    color("#000080")
    begin_fill()
    circle(50)
    end_fill()
    penup()
    left(90)
    forward(75)
    pendown()
    color("yellow")
    begin_fill()
    for n in range(20):
        right(50)
        right(140)
        forward(57)
    end_fill()
    penup()
    forward(200)
    pendown()
CrescentAndStar()



done()