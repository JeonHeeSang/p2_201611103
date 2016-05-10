mylist=list()
mylist=[["Coffee","Water","Milk","Icecream"],
        ["Espresso","No","No","No"],
        ["Long Black","Yes","No","No"],
        ["Flat White","No","Yes","No"],
        ["Cappuccino","No","Yes - Frothy","No"],
        ["Affogato","No","No","Yes"]]
data=mylist[1:] 
sum=0
for i in data:
    if i[2].upper()=='YES':
        sum=sum+1
print "percent:", float(sum)/float(len(data))
input()