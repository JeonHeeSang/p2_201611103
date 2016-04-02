﻿marks=raw_input("input your Score(0~100):")
marks=float(marksTmp)
print "your Score is:", marksTmp

def convertScoretoGrade(marks):
    if 90<=float(marks)<=100:
        grade="A"
    if 80<=float(marks)<90:
        grade="B"
    if 70<=float(marks)<80:
        grade="C"
    if 60<=float(marks)<70:
        grade="D"
    if  float(marks)<60:
        print "Congratulations!! you are F Grade!!"
        grade="F"
    else:
        print "Score's can not be higher than 100 or lower than 0"
        return grade

result=convertScoretoGrade(marks)
print "your grade is %s" %result
        