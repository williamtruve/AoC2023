from collections import defaultdict
from aocd import get_data, submit
import re
import numpy as np
from utils.aocutils import *
ERROR = False

data = get_data(day=4, year=2023).splitlines()


#print(data)
#data = open("day4/test.txt","r").read().splitlines()
#data = open("day4/input.txt","r").read()
pattern = r"\d+"

matrix = []
for lin in data:
    matrix.append(lin)

total_sum = 0
def return1():
    return 1
counterDict = defaultdict(return1)
for ix, line in enumerate(matrix):
    splitData = line.strip().split(":")
    cardNumber = int(splitData[0].split(" ")[-1])
    #print("cardNumber", cardNumber)
    #print(splitData)
    allValues = splitData[-1].split("|")

    winningNumbers = allValues[0]
    matchesWinning = re.finditer(pattern, winningNumbers)
    matchesWinning = [m.group() for m in matchesWinning]

    testNumbers = allValues[1]
    matchesTest = re.finditer(pattern, testNumbers)
    matchesTest = [m.group() for m in matchesTest]

    tmpValue = 0
    #print(matchesWinning)
    #print(matchesTest)
    for number in matchesWinning:
        if number in matchesTest:
            tmpValue += 1

    #print("tmpValue", tmpValue)
    
    numberOfCopies = counterDict[cardNumber]
    if tmpValue >0:
        for yx in range(cardNumber + 1, cardNumber + tmpValue + 1):
            counterDict[yx] += numberOfCopies
            #matrix.append(data[yx-1])

total_sum = sum(counterDict.values())
print(total_sum)
#submit(answer=total_sum, day=4, year=2023)
