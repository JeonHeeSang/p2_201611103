def leapyear():
       year=input("User input year:")
       if (year%4==0)and (year%100!=0 or year%400==0):
       print "Leap year"
       else:
           print "Not Leap year"
def updowngame():
       import random
       select=raw_input("input range number 1~100: ")
       s1=int(select)
       r1=random.randrange(1,s1+1)
       print "range is 1~%f" % s1
       def st():
           selectr=raw_input("input number you want: ")
           s3=int(select)
           global s3
       def mp():
            if(s3==r1):
                  print "nice"
            else:
                if(s3>r1):
                   print "low"
                   st()
                   mp()
            elif(s3<r1):
                   print "high"
                   st()
                   mp()
            else:
                 print "error"
    st()
    mp()
       

def lab6():
        leapyear()
        updowngame()   
def main():
        lab6()

if _name_=="_main_":
       main()