import csv
import numpy as np
import math

K=5 #环境抵抗力

def readData():
    lix = list()
    liy = list()
    litag=list()
    f = open('Combination.CSV', 'rt').readlines()
    d = csv.reader(f)
    for line in d:
        lix.append(float(line[7]))
        liy.append(float(line[8]))
        litag.append(line[6])
        pass
    return (lix,liy,litag)

def calYear(q):
    year = 0
    while True:
        a = q/5.0
        temp = a-a/(1+a**(math.e-11.66*year))
        if temp<=(a/100):
            return year
        year = year + 1

y,x,tags=readData()

beeMap=np.zeros((45,54))
yearMap=np.zeros((45,54))
yearMap = yearMap-2
assert len(x)==len(y)
dataList=[]
for i in range(len(x)):
    dataList.append([x[i],y[i],tags[i]])

positive=list()
for item in dataList:
    loc_x=int((item[0]+124.8)//0.15)
    loc_y=int((item[1]-45.3)//0.1)
    if item[2]=='Positive ID':
        positive.append([loc_y,loc_x])
        beeMap[loc_y][loc_x] += 1
    else:
        beeMap[loc_y][loc_x] += 1
#print(beeMap.tolist())
print("Setting positive")
for item in positive:
    if beeMap[item[0]][item[1]] != -1:
        if beeMap[item[0]][item[1]] <= 5:
            yearMap[item[0]][item[1]]=1
            beeMap[item[0]][item[1]] = -1
            continue
        yearMap[item[0]][item[1]]=calYear(beeMap[item[0]][item[1]])
        # print(yearMap[item[0]][item[1]])
        beeMap[item[0]][item[1]]=-1
print('Positive settled')

beeMap = np.flip(beeMap,0)
yearMap = np.flip(yearMap,0)
#print(beeMap.tolist())
# for item in beeMap.tolist():
#     print(item)
beeMap = beeMap.tolist()
#print(np.sum(beeMap))

def spread(beeMap,number,jugNumber):
    for i in range(1,44):
        for j in range(1,53):
            if yearMap[i][j] == 0 or yearMap[i][j] == -1:
                yearMap[i][j] = -1
                compList = [beeMap[i-1][j],beeMap[i+1][j],beeMap[i][j-1],beeMap[i][j+1]]
                state = compList.index(max(compList))
                maxTreasure = max(compList)
                if maxTreasure>K:
                    i_station = 0
                    j_station = 0
                    if state == 0:
                        i_station = -1
                    elif state == 1:
                        i_station = 1
                    elif state == 2:
                        j_station = -1
                    elif state == 3:
                        j_station = 1
                    if yearMap[i+i_station][j+j_station] == -2:
                        yearMap[i+i_station][j+j_station] = calYear(beeMap[i+i_station][j+j_station])
                    beeMap[i+i_station][j+j_station]=-number
    return beeMap

def yearPass(yearMap):
    print('Year passing')
    for i in range(1, 44):
        for j in range(1, 53):
            if yearMap[i][j] != -2 and yearMap[i][j] != -1:
                yearMap[i][j] -= 1

for i in range(1,35):
    print('Year',i)
    beeMap = spread(beeMap,i+1,list(range(-i,0)))
    yearPass(yearMap)

print(beeMap)
# for item in beeMap:
#     print(item)
# for i in range(20):
#     print('')
#
# for item in yearMap.tolist():
#     print(item)

