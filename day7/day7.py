from collections import defaultdict
from aocd import get_data, submit
import re
import numpy as np
ERROR = False
import sys
from tqdm import tqdm
data = open("day7/input.txt","r").readlines()

#data = open("day7/test.txt","r").readlines()
noWins = []
onePairs = []
twoPairs = []
three_of_a_kind = []
full_house  = []
four_of_a_kind = []
five_of_a_kind = []

def addHandToRankSet(handDict):
    hand = handDict['hand']
    countJs = 0
    for j in hand:
        if j == 'J':
            countJs += 1
    counter = defaultdict(int)
    for i in hand:
        if i != "J":
            counter[str(i)] += 1
    if countJs != 0:
        print(hand)
        maxNum = 0
        chosen = ""
        for k, v in counter.items():
            if v > maxNum:
                maxNum = v
                chosen = k
        hand = hand.replace("J", chosen)
        print(hand)
        print()
    if countJs == 5:
        hand = "22222"
    handSet = list(set(hand))

    if len(set(hand)) == 1:
        five_of_a_kind.append(handDict)
    elif len(set(hand)) == 2:
        char1 = handSet[0]
        c1 = 0
        char2 = handSet[1]
        c2 = 0
        for c in hand:
            if c == char1:
                c1 += 1
            else:
                c2 += 1
        if c1 == 4 or c2 == 4:
            four_of_a_kind.append(handDict)
        else:
            full_house.append(handDict)
    elif len(set(hand)) == 3:
        char1 = handSet[0]
        c1 = 0
        char2 = handSet[1]
        c2 = 0
        char3 = handSet[2]
        c3 = 0
        for c in hand:
            if c == char1:
                c1 += 1
            elif c == char2:
                c2 += 1
            else:
                c3 += 1
        if c1 == 3 or c2 == 3 or c3 == 3:
            three_of_a_kind.append(handDict)
        else:
            twoPairs.append(handDict)
    elif len(set(hand)) == 4:
        onePairs.append(handDict)
    else:
        noWins.append(handDict)

pairs = []
liens = []
import sys
for line in data:
    liens.append(line)

    tmpDict = {}
    line = line.strip().split()
    hand = line[0]
    bid = int(line[1])
    tmpDict['hand'] = hand
    tmpDict['bid'] = bid
    tmpDict['sort'] = None

    pairs.append(tmpDict)



for p in pairs:
    addHandToRankSet(p)

allSets = [five_of_a_kind, four_of_a_kind, full_house,  three_of_a_kind, twoPairs, onePairs, noWins]

def gethand(dicte):
    return dicte['sort']

#SORT_ORDER = {"A": 0, "K": 1, "Q": 2 , "J": 3, "T": 4,"9": 5,"8": 6,"7": 7,"6": 8,"5": 9,"4": 10, "3": 11,"2": 12}
SORT_ORDER = {"A": 0, "K": 1, "Q": 2 , "T": 3,"9": 4,"8": 5,"7": 6,"6": 7,"5": 8,"4": 9, "3": 10,"2": 11, "J": 12}


allHandsSorted = []
for a in allSets:
    for handdi in a:
        handdi['sort'] = [SORT_ORDER[key] for key in handdi['hand']]
        
for d in allSets:
    for y in sorted(d, key=gethand):
        allHandsSorted.append(y)
total_sum = 0
print(len(allHandsSorted)-1)
for ix in range(len(allHandsSorted)-1, -1 , - 1):
    total_sum += allHandsSorted[len(allHandsSorted)-1-ix]['bid']*(ix+1)
print(total_sum)