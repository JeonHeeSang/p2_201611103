import turtle
wn=turtle.Screen()
wn.bgpic("C:\Users\user\Desktop/myMaze.gif")
t1=turtle.Turtle()
t1.penup()
t1.goto(-250,250)
t1.right(90)
def keyup():
    t1.forward(100)
def keydown():
    t1.back(100)
def keyleft():
    t1.left(90)
def keyright():
    t1.right(90)
def mousegoto(x,y):
    t1.setpos(x,y)
def addkeys():
    wn.onkey(keyup,"Up")
    wn.onkey(keydown,"Down") 
    wn.onkey(keyleft,"Left")
    wn.onkey(keyright,"Right")
def addmouse():
    wn.onclick(mousegoto)    
addkeys()
addmouse()
wn.listen()
turtle.mainloop()