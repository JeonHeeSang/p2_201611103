import turtle 
wn=turtle.Screen()
wn.bgcolor("black")
t1=turtle.Turtle()
t1.shape("turtle")
t1.color("gray")
t1.left(90)
t1.penup()
t1.goto(-80,-150)
t1.write("start")
import turtle
wn=turtle.Screen()
t2=turtle.Turtle()
t2.shape("turtle")
t2.color("Red")
t2.left(90)
import turtle
t3=turtle.Turtle()
t3.shape("turtle")
t3.color("Blue")
t3.left(90)
import turtle
t4=turtle.Turtle()
t4.shape("turtle")
t4.color("Yellow")
t4.left(90)
import turtle
t5=turtle.Turtle()
t5.shape("turtle")
t5.color("Purple")
t5.left(90)
import turtle
s1=turtle.Turtle()
s1.shape("turtle")
s1.color("Green")
s1.penup()
s1.speed(3)
import turtle
s2=turtle.Turtle()
s2.shape("turtle")
s2.color("orange")
s2.penup()
s2.goto(100,-70)
s2.left(90)
import turtle
s3=turtle.Turtle()
s3.shape("turtle")
s3.color("White")
s3.penup()
s3.goto(-200,90)
s3.left(90)
import turtle
s4=turtle.Turtle()
s4.shape("turtle")
s4.color("Pink")
s4.penup()
s4.goto(410,10)
s4.pendown()
size=120
def getCoordsFromFile():
    frec=open('shape.txt')
    coords=[]
    for line in frec:
        line1=line.split(',')
        coords.append([line1[0],line1[1],line1[2],line1[3],line1[4],line1[5],line1[6],line1[7],line1[8],line1[9]])
    frec.close()
    return coords
mycoords=getCoordsFromFile()

def drawfigure(mycoords):
    for coord in mycoords:
        x1=int(coord[0])
        x2=int(coord[2])
        x3=int(coord[4])
        x4=int(coord[6])
        x5=int(coord[8])
        y1=int(coord[1])
        y2=int(coord[3])
        y3=int(coord[5])
        y4=int(coord[7])
        y5=int(coord[9])
    print x1,y1,x2,y2,x3,y3,x4,y4  
    s1.penup()
    s1.goto(x1,y1)
    s1.pendown()
    s1.pencolor("Red")
    for i in range(0,3):
        s1.fd(size)
        s1.right(120)
    t2.penup()
    t2.goto(-390,160)
    s1.penup()
    s1.goto(x2,y2)
    s1.pendown()
    s1.pencolor("Blue")
    for i in range(0,5):
        s1.fd(size)
        s1.right(72)
    t3.penup()
    t3.goto(-100,130)
    s1.penup()
    s1.goto(x4,y4)
    s1.pendown()
    s1.pencolor("Yellow")
    for i in range(0,4):
        s1.fd(size)
        s1.right(90)
    t4.penup()
    t4.goto(-340,-10)
    s1.penup()
    s1.goto(x5,y5)
    s1.pendown()
    s1.pencolor("Purple")
    for i in range(0,6):
        s1.fd(size)
        s1.right(60)  
    t5.penup()
    t5.goto(50,-30)
    s1.penup()
    s1.goto(x3,y3)
    s1.pendown()
    s1.pencolor("Green")
    for i in range(0,5):
        s1.fd(size)
        s1.right(144)
    s1.penup()
    s1.goto(90,155)
    s1.left(90)    
drawfigure(mycoords) 
def giyuk(size):
    s4.fd(size)
    s4.right(90)
    s4.fd(size)
turnBy=45
oldpos=s4.pos()
oldhead=s4.heading()
giyuk(size)
x=float()
y=float()
def up(): 
    t1.forward(20)
    (x,y)=t1.pos()
    if -395<x<-375 and 155<y<175:
        s4.penup()
        s4.setpos(oldpos)
        s4.setheading(oldhead+turnBy)
        s4.pendown()
        giyuk(size)
    elif -105<x<-85 and 120<y<140:
        s4.penup()
        s4.setpos(oldpos)
        s4.setheading(oldhead+turnBy+turnBy)
        s4.pendown()
        giyuk(size)
    elif -350<x<-330 and -20<y<0:
        s4.penup()
        s4.setpos(oldpos)
        s4.setheading(oldhead+turnBy+turnBy+turnBy)
        s4.pendown()
        giyuk(size)
    elif 40<x<60 and -35<y<-15:
        s4.penup()
        s4.setpos(oldpos)
        s4.setheading(oldhead+turnBy+turnBy+turnBy+turnBy)
        s4.pendown()
        giyuk(size)
    elif 80<x<100 and 150<y<170:
        s4.penup()
        s4.setpos(oldpos)
        s4.setheading(oldhead+turnBy+turnBy+turnBy+turnBy+turnBy)
        s4.pendown()
        giyuk(size)
    elif 90<x<110 and -75<y<-55:
        s4.penup()
        s4.setpos(oldpos)
        s4.setheading(oldhead+turnBy+turnBy+turnBy+turnBy+turnBy+turnBy)
        s4.pendown()
        giyuk(size)
    elif -205<x<-185 and 80<y<100:    
        s4.penup()
        s4.setpos(oldpos)
        s4.setheading(oldhead+turnBy+turnBy+turnBy+turnBy+turnBy+turnBy+turnBy)
        s4.pendown()
        giyuk(size)     
    elif -90<x<-70 and -160<y<-140:
        print "Windmill completion"
def le():  
    t1.left(45)  
def ri():  
    t1.right(45)  
def do():  
    t1.back(20)
    
wn.onkey(up, "Up")  
wn.onkey(le, "Left")  
wn.onkey(ri, "Right")  
wn.onkey(do, "Down")  
wn.listen()  
wn.exitonclick()