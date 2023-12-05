from collections import defaultdict
from aocd import get_data, submit
import re
import numpy as np
ERROR = False
import sys

data = open("day5/inp.txt","r").readlines()
seeds = "630335678 71155519 260178142 125005421 1548082684 519777283 4104586697 30692976 1018893962 410959790 3570781652 45062110 74139777 106006724 3262608046 213460151 3022784256 121993130 2138898608 36769984"

#data = open("day5/test.txt","r").readlines()
#seeds = "79 14 55 13"
listDict = defaultdict(list)

seeds = seeds.split()

for ix in range(0, len(seeds)-1, 2):
    ele = int(seeds[ix])
    range1 = int(seeds[ix+1])
    listDict['seed'].append((ele, ele+range1-1))

#humidity-to-location map:
#3880387060 2052152805 97611299
#destination, source, range

pattern1 = r"(?P<source>\w+)-to-(?P<target>\w+)"

pattern2 = r"(?P<targetRange>\d+)\s+(?P<sourceRange>\d+)\s+(?P<ranges>\d+)"
bigDict = defaultdict(list)
source = ""
target = ""
sr_start = 0
sr_end = 0
tr_start = 0
tr_end = 0
tmpList = []
sourceToTargetDict = {}
ranges = 0
allDicts = []

for d in data:
    mapper = re.search(pattern1, d)
    mapRanges = re.search(pattern2, d)
    if mapper:

        sourceToTargetDict = {}
        source = mapper.groupdict()['source']
        target = mapper.groupdict()['target']
        tmpList = listDict[source]
        for t in tmpList:
            sourceToTargetDict[t] = t

    elif mapRanges:
        sr_start = int(mapRanges.groupdict()['sourceRange'])
        tr_start =int(mapRanges.groupdict()['targetRange'])
        ranges = int(mapRanges.groupdict()['ranges'])-1
        sr_end = sr_start + ranges
        tr_end = tr_start + ranges

        for element in tmpList:
            if  sr_start <= int(element[0]) and int(element[1]) <= sr_end:
                diff = int(element[0]) - sr_start
                sourceToTargetDict[(element[0], element[1])] = (tr_start + diff, tr_start + diff +  (int(element[1]) - int(element[0])))

            elif  int(element[0]) < sr_start and int(element[1]) >= sr_start and int(element[1]) <= sr_end:
                del sourceToTargetDict[element]
                sourceToTargetDict[(element[0],sr_start-1)] = (element[0],sr_start-1)

                diff = int(element[1]) - sr_start
                sourceToTargetDict[(sr_start, sr_start + diff)] = (tr_start, tr_start + diff)

            elif  int(element[0]) > sr_start and int(element[0]) <= sr_end and int(element[1]) > sr_end:
                del sourceToTargetDict[element]
                sourceToTargetDict[(sr_end+1, element[1])] = (sr_end+1, element[1])

                diff = int(element[0]) - sr_start
                sourceToTargetDict[(element[0],sr_end)] = (tr_start+diff, tr_end)

            elif  int(element[0]) < sr_start and sr_end < int(element[1]):
                del sourceToTargetDict[element]
                sourceToTargetDict[(element[0], sr_start-1)] = (element[0], sr_start-1)
                sourceToTargetDict[(sr_start, sr_end)] = (tr_end, tr_start)

                sourceToTargetDict[(tr_end+1, element[1])] = (tr_end+1, element[1])
        listDict[target] = list(sourceToTargetDict.keys())
        tmpList = listDict[target]

    
    else:
        listDict[target] = list(sourceToTargetDict.values())


#        print(sourceRange)
 #       print(targetRange)
  #      print(ranges)
listDict[target] = list(sourceToTargetDict.values())

smallest = 10000000000000000000
for tup in listDict['location']:
    if tup[0] < smallest:
        smallest = tup[0]
print(smallest)
ans = (listDict['location'])

        