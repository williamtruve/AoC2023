from collections import defaultdict
from aocd import get_data, submit
import re
import numpy as np
ERROR = False
import sys
from teseter import *

data = open("day5/inp.txt","r").readlines()
seeds = "630335678 71155519 260178142 125005421 1548082684 519777283 4104586697 30692976 1018893962 410959790 3570781652 45062110 74139777 106006724 3262608046 213460151 3022784256 121993130 2138898608 36769984"

data = open("day5/test.txt","r").readlines()
seeds = "79 14 55 13"
rangeDict = defaultdict(list)

seeds = seeds.split()

for ix in range(0, len(seeds)-1, 2):
    ele = int(seeds[ix])
    range1 = int(seeds[ix+1])-1
    rangeDict['seed'].append((ele, ele+range1))

#humidity-to-location map:
#3880387060 2052152805 97611299
#destination, source, range


source = ""
target = ""
sr_start = 0
sr_end = 0
tr_start = 0
tr_end = 0
ranges = 0
rangeToRange = {}
# Pattern to extract source-to-target maps
pattern1 = r"(?P<source>\w+)-to-(?P<target>\w+)"

#Pattern to extract targetrange, sourcerange, and length of range
pattern2 = r"(?P<targetRange>\d+)\s+(?P<sourceRange>\d+)\s+(?P<ranges>\d+)"
for d in data:
    mapper = re.search(pattern1, d)
    mapRanges = re.search(pattern2, d)

    if mapper:
        source = mapper.groupdict()['source']
        target = mapper.groupdict()['target']
        print(source, "-->", target)
        print("rd of source", rangeDict[source])
        rangeToRange = {}
        for rtr in rangeDict[source]:
            rangeToRange[rtr] = rtr

    elif mapRanges:
        ranges = int(mapRanges.groupdict()['ranges'])
        sourceRange = ((int(mapRanges.groupdict()['sourceRange']),int(mapRanges.groupdict()['sourceRange'])+ranges))
        targetRange = ((int(mapRanges.groupdict()['targetRange']), int(mapRanges.groupdict()['targetRange'])+ranges))

        for rx in rangeDict[source]:
            print("sr, tr", sourceRange, targetRange, rx)
            del rangeToRange[rx]

            disjoint_result = disjoint_ranges(rx, sourceRange)
            print(disjoint_result)
            diff = intersect_ranges(rx,sourceRange)
            print(diff)

            joined_ranges = [*diff, *disjoint_result]
            print(joined_ranges)
            mapped_ranges = [map_range(ry, sourceRange,targetRange) for ry in joined_ranges]
            print("mapped_ranges", mapped_ranges)
            print()
            for jx, mx in zip(joined_ranges, mapped_ranges):
                print(jx, mx)
                rangeToRange[jx] = mx
        rangeDict[source] = (list(rangeToRange.keys()))
    else:
        rangeDict[target] = (list(rangeToRange.values()))
        #sys.exit()
#        print(sourceRange)
 #       print(targetRange)
  #      print(ranges)

rangeDict[target].extend(list(rangeToRange.values()))

smallest = 10000000000000000000
for tup in rangeDict['location']:
    if tup[0] < smallest:
        smallest = tup[0]
print(smallest)

        