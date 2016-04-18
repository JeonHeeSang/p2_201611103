import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
﻿def drawSquareAt(size, pos):
    t1.penup()
    t1.setpos(pos)
    t1.pendown()
    tracks=list()
    for i in range(0,4):
        tracks.append(t1.pos())
        t1.forward(size)
        t1.right(90)
    return tracks
import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
xtracks=input("input x pos:")
ytracks=input("input y pos:")
def drawSquareFrom(xtracks,ytracks):
    x=((xtracks,ytracks),(xtracks+50,ytracks),(xtracks+50,ytracks+50),(xtracks,ytracks+50),(xtracks,ytracks))
    t1.penup()
    t1.goto(x[0])
    t1.pendown()
    for i in range(0,5):
        t1.goto(x[i])        
def lab7A():
    drawSquareAt(size,pos)
    print tracks
def lab7B():
    xtracks=input("input x pos:")
    ytracks=input("input y pos:")
    drawSquareFrom(xtracks,ytracks)
def main:
    lab7A()
    lab7B()
if_name_=="_main_":
     main()
