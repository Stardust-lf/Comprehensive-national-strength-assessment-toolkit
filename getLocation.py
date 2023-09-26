import csv
def readData():
    lix = list()
    f = open('Combination.CSV', 'rt').readlines()
    d = csv.reader(f)
    for line in d:
        linflo = list()
        for ite in line:
            linflo.append(ite.replace(' ',''))
        lix.append(linflo[:-1])
        pass
    return lix[1:]

def readResultData():
    lix = list()
    f = open('result.csv', 'rt').readlines()
    d = csv.reader(f)
    for line in d:
        if float(line[1]) >= 0.5:
            lix.append(line[0].replace(' ',''))
        pass
    return lix

data = readData()
result = readResultData()
for item in result:
    for it in data:
        if it[2][3:7]==item[3:7]:
            #print(item)
            print(it[1][:4])
            #print(it[0])
