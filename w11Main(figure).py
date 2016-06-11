import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
t2=turtle.Turtle()

import math

center=(170,200)

coord=[(100,-130),(250,20)]

line1=[(70,-200),(250,-200)]
pos1=line1[0]
pos2=line1[1]

radius=100




def t1_start():
    t1.penup()
    t1.setpos(-250,0)
    t1.pendown()


def Circle():
    t2.penup()
    t2.setpos(160,100)
    t2.pendown()
    t2.circle(80)

def Rectangle():
    t2.penup()
    t2.setpos(100,20)
    t2.pendown()
    for i in range(4):
        t2.fd(100)
        t2.right(90)
        
def Line():
    t2.penup()
    t2.setpos(70,-200)
    t2.pendown()
    t2.fd(150)
    

    
def isInCircle(center,radius,pos):
    c=center
    return 0<(math.sqrt(math.pow(c[0]-pos[0],2)+ math.pow(c[1]-pos[1],2)))<(radius)
    
def isInRectangle(curpos,coord):
    xs=coord[0][0]
    xe=coord[1][0]
    ys=coord[0][1]
    ye=coord[1][1]
    return xs<=curpos[0]<=xe and ys<=curpos[1]<=ye

def isOnLine(pt,pos1,pos2):
    x1=pos1[0]-2
    y1=pos1[1]-2
    x2=pos2[0]+2
    y2=pos2[1]+2
    return isInRectangle(pt,[(x1,y1),(x2,y2)])




def keyup():
    pt=t1.pos()
    t1.forward(10)
    if isInCircle(center,radius,pt):
        t2.pencolor("red")
        Circle()
        t1_start()
    elif isInRectangle(pt,coord):
        t2.pencolor("red")
        Rectangle()
        t1_start()
    elif isOnLine(pt,pos1,pos2):
        t2.pencolor("red")
        Line()
        t1_start()

        
def keyleft():
    t1.left(90)
    
def keyright():
    t1.right(90)
    
def keydown():
    pt=t1.pos()
    t1.back(10)
    if isInCircle(center,radius,pt):
        t2.pencolor("red")
        Circle()
        t1_start()
    elif isInRectangle(pt,coord):
        t2.pencolor("red")
        Rectangle()
        t1_start()
    elif isOnLine(pt,pos1,pos2):
        t2.pencolor("red")
        Line()
        t1_start()
        
def addKeys():
    wn.onkey(keyup, "Up")
    wn.onkey(keyleft, "Left")
    wn.onkey(keyright, "Right")
    wn.onkey(keydown, "Down")
    wn.onkey(wn.bye, "q")

def gamePlay_figure():
    t1_start()
    Circle()
    Rectangle()
    Line()
    addKeys()

    
def lab11():
    gamePlay_figure()   
    wn.listen()
    turtle.mainloop()
    
    
def main():
    lab11()

if __name__=="__main__":
    main()
