Mylist=list()
Mylist=[["English", 100],
       ["Math", 200],
       ["English", 200],
       ["Math", 200],
       ["English", 100],
       ["Math", 300]]
Esum=0
Msum=0
en=0
ma=0
for i in Mylist:
    if i[0]=="English":
        en+=1
    elif i[0]=="Math":
        ma+=1
for i in Mylist:
    if i[0]=="English":
        Esum+=i[1]
    elif i[0]=="Math":
        Msum+=i[1]        
print  "English Total:", Esum        
print "Math Total:", Msum
print "English average:", Esum/en
print "Math average:", Msum/ma
input()