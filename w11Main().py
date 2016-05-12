dataG=[[13.1, 37.1],
     [10.6, 34.6],
     [27.1, 40.0],
     [16.2, 37.8],
     [11.4, 29.8],
     [12.2, 26.5],
     [13.5, 29.7],
     [13.7, 37.6]]
dataN=[[8.7, 1.5],
      [13.4, 1.9],
      [2.9, 1.5],
      [6.8, 0.8],
      [14.8, 4.9],
      [14.9, 4.4],
      [11.1, 2.4],
      [4.1, 1.2]]
sumG=0
sumN=0
for i in dataG:
    sumG=sumG+i[0]+i[1]
for c in dataN:
    sumN=sumN+c[0]+c[1]
print "dataG sum:",sumG, "dataN sum:",sumN
print "dataG average:",float(sumG/len(dataG)), "dataN average:",float(sumN/len(dataN))
input()