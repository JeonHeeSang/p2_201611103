import math
populations=tuple()
populations=[(74425, 76326), (61164, 61636),(109688, 115744), (144796, 146776), (174996, 181676), (177841, 177434), (204630, 205980), (223373, 232245), (161055, 166130), (171576, 176735),(279169, 293772),(239450, 251066), (148690, 156510), (182977, 196992), (237792, 242641), (283869, 296762), (209344, 210282), (118965, 114441), (186503, 186856), (195734, 203014), (254381, 249472), (212401, 229111), (271654, 295354), (319197, 335045), (229829, 231671)]
Mensum=0
Womensum=0
Menaverage=0
Womenaverage=0
for i in populations:
    Mensum+= i[0]
    Womensum+= i[1]
print "M total:", Mensum
print "W total:", Womensum
Menaverage=Mensum/len(populations)
Womenaverage=Womensum/len(populations)
print "M average:", Menaverage
print "W average:", Womenaverage
mylist=list()
for c in populations:
    mylist.append(c[0]+c[1])
print mylist
import matplotlib 
import matplotlib.pyplot as plt
print populations
plt.bar(range(0,len(mylist)),mylist, align='center')
plt.show()
input()