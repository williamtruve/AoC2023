from collections import defaultdict
from operator import indexOf
from aocd import get_data, submit
import re
import numpy as np
from sympy import false, true
ERROR = False
import sys
from tqdm import tqdm
data = open("day8/inp.txt","r").readlines()

#data = open("day8/test.txt","r").readlines()

print(data)

instructions = data[0].strip()
print(instructions)
#VHL = (HPR, DTN)
pattern = r"(?P<source>\w+)\s+=\s+\((?P<left>\w+),\s+(?P<right>\w+)"
mapper = defaultdict(defaultdict)
starting_positions = []
end_positions = []
for d in data:
    x = re.search(pattern, d)
    if x:
        source = x.groupdict()['source']
        left = x.groupdict()['left']
        right = x.groupdict()['right']
        mapper[source]['L'] = left
        mapper[source]['R'] = right
        mapper[source]['steps_before'] = 0
        mapper[source]['loop_length'] = 0

        if source[-1] == "A":
            starting_positions.append(source)
        if source[-1] == "Z":
            end_positions.append(source)

steps_before_loop = 0
for sp in starting_positions:
    sp_to_goal_found = False   
    current_pos = sp
    path = [(current_pos, 0)]
    c = 0
    wc = 0
    found_path = False
    while True:
        print(f"searching for path for pos {sp}, times {wc}")
        wc += 1
        for ix, ins in enumerate(instructions):
            c += 1
            current_pos = mapper[current_pos][ins]
            if (current_pos, ix) in path:
                #print(current_pos, ix)
                #print(path)
                #print("loop found!!")
                mapper[sp]['steps_before'] = steps_before_loop
                found_path = True
                path.append((current_pos, ix))
                start_of_path = indexOf(path, (current_pos, ix))
                mapper[sp]['path'] = path[start_of_path:]
                mapper[sp]['stp'] = start_of_path

                mapper[sp]['full_path'] = path

                mapper[sp]['loop_length'] = len(path[start_of_path:])-1

                #print(steps_before_loop)
                #print(c - steps_before_loop + 1)
                #sys.exit()
            if found_path:
                break
            path.append((current_pos, ix))
            if current_pos[-1] == "Z" and not sp_to_goal_found:
                steps_before_loop = c
        if found_path:
            break
for p in starting_positions:
    mapper[p]['zs'] = []
    for yx, pos in enumerate(mapper[p]['path']):
        if pos[0][-1] == "Z":
            mapper[p]['zs'].append(yx+mapper[p]['stp'])
    
    print("fp",mapper[p]['full_path'])
    print("stp",mapper[p]['stp'])

    print("path,",mapper[p]['full_path'][mapper[p]['stp']:])
    print("path",mapper[p]['path'])

    
    mapper[p]['zs'] = np.array(mapper[p]['zs'])
    print("loop_lengt", mapper[p]['loop_length'])
    print("zs", mapper[p]['zs'])

onZ = []
k = 1
wc = 0
print()
print()
a = []

for p in starting_positions:
    k *= mapper[p]['loop_length']
    print("loop_lengt", mapper[p]['loop_length'])
    a.append(mapper[p]['loop_length'])
    print("zs", mapper[p]['zs'])



print(k)
from math import gcd
lcm = 1
for i in a:
    lcm = lcm*i//gcd(lcm, i)
print(lcm)