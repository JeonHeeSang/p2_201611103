import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
def keyup():
    t1.forward(50)
def keydown():
    t1.back(50)

def keyleft():
    t1.left(90)

def keyright():
    t1.right(90)

def mousegoto(x,y):
    t1.setpos(x,y)
    t1.pos=(x,y)
    if 0<x<50 and y==0:
        print "Correct"
def addkeys():
    wn.onkey(keyup,"Up")
    wn.onkey(keydown,"Down") 
    wn.onkey(keyleft,"Left")
    wn.onkey(keyright,"Right")
def addMouse():
     wn.onclick(mousegoto)
addkeys()
addMouse()
wn.listen()
raw_input("Press the Enter")