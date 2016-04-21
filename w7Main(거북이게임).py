def turtlegame():
    
    import turtle 
    wn=turtle.Screen()
    t1=turtle.Turtle()
    t1.shape("turtle")
    t1.left(90)
    import turtle
    s1=turtle.Turtle()
    s1.shape("turtle")
    t1.penup()
    s1.penup()
    t1.goto(0,-150)
    s1.speed(3)
    score=0
    size=raw_input("input size 100~150:")
    d1=float(size)
    sum=0
    s1.goto(-350,200)
    for i in range(0,3):
        s1.pendown()
        s1.fd(d1)
        s1.right(120)    
    s1.penup()
    s1.goto(-50,200)
    for i in range(0,5):
        s1.pendown()
        s1.fd(d1)
        s1.right(72)
    s1.penup()
    s1.goto(200,200)
    for i in range(0,5):
        s1.pendown()
        s1.fd(d1)
        s1.right(144)
    s1.pendown()    

    select=raw_input("Where will you go?:")
    if(select=="triangle"):
        t1.goto(-300,150)

    elif(select=="pentagon"):
        t1.goto(0,150)

    elif(select=="star"):
        t1.goto(250,180)
    if(t1.pos==s1.pos):
        score=score+1

def lab7():
    turtlegame()
def main():
    lab7()
if __name__=="__main__":
       main()