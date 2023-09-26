import re
import csv
def readData():
    lix = list()
    f = open('Combination.CSV', 'rt').readlines()
    d = csv.reader(f)
    for line in d:
        linflo = list()
        for ite in line:
            linflo.append(ite)
        lix.append(linflo[:-1])
        pass
    return lix[1:]

data = readData()
word='honey|mellifera|Apis'
li = list()
for item in data:
    if re.search(word,item[5],re.IGNORECASE) is not None:
        li.append(item[2])
        print(item[5])
        pass
    pass
print(li)
print(len(li))
