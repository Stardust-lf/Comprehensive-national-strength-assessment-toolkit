import csv
import numpy as np
import math

def calYear(q):
    year = 0
    while True:
        a = q/5.0
        temp = a-a/(1+a**(math.e-11.66*year))
        if temp<=(a/100):
            return (year,a-temp)
        year = year + 1

data = [[49.0, [36, 14]], [74.0, [36, 13]], [4.0, [38, 5]], [4.0, [38, 5]], [4.0, [38, 5]], [4.0, [38, 5]], [5.0, [37, 13]], [-1.0, [36, 13]]]

for item in data:
    if item[0]<=5:
        print(item[1],'will die')
    else:
        print(calYear(item[0]),item[1])