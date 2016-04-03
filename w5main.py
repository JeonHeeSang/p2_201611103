def game():
    print "Let's play R S P Game"
    UA=raw_input("A:")
    UB=raw_input("B:")
    def N(U):
        if(U=="R"):
            return 1.0
        elif(U=="S"):
            return 2.0
        elif(U=="P"):
            return 4.0
        else:
            print "Input Error"
    p=N(UA)/N(UB)
    if(p==1.0):
        print "draws"
    elif(p==0.5):
        print "A wins"
    elif(p==0.25):
        print "B wins"
    elif(p==2):
        print "B wins"
    elif(p==4):
        print "A wins"