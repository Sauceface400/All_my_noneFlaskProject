from turtle import *

speed(3)
penup()
goto(-250,200)
pendown()

bgcolor("black")
#===========================THE BASE OF THE FLAG OF THE GREEN PART=============================
def kotak(length,length1,height):
    for h in range(2):
        color("#006600")
        begin_fill()
        forward(length)
        right(height)
        forward(length1)
        right(height)
        end_fill()

kotak(500,250,90)
#==============================THE SECOND BASE OF THE FLAG, THE WHITE PART============================
def kotak_kedua(length,length2,height):
    for h in range(2):
        color("white")
        begin_fill()
        forward(length)
        right(height)
        forward(length2)
        right(height)
        end_fill()        

kotak_kedua(125,250,90)
#===========================THE CRESCENT AND THE STAR===============================================
penup()
goto(10,20)
pendown()
color("white")
begin_fill()
circle(65)
end_fill()

penup()
goto(35,35)
pendown()
color("#006600")
begin_fill()
circle(65)
end_fill()

penup()
goto(30,120)
pendown()
right(45)
color("white")
begin_fill()
for j in range(5):
    forward(40)
    right(144)
end_fill()
#=============================THE TEXT OF THE NAME OF PAKISTAN====================================
penup()
goto(-330,-200)
pendown()
write("PAKISTAN FLAG BABY I SUPPORT", font=("Arial",30))
done()