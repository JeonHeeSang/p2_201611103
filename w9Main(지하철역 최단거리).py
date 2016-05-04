import math
Locations=tuple()
myList=list()
(x1,y1)=(37.575765,126.973626)
Locations=[(37.576573,126.985536),(37.588826,126.944051),(37.574577,126.957754),(37.619012,126.921141),(37.571618,126.976551)]
mylist=list()
for i in Locations:
    mylist.append(math.sqrt((x1-i[0])**2+(y1-i[1])**2))
print min(mylist)
input()
