from collections import defaultdict
from aocd import get_data, submit
import re
import numpy as np
ERROR = False
import sys
from tqdm import tqdm
data = open("day6/input.txt","r").readlines()

data = open("day6/test.txt","r").readlines()
times = [56717999]
dists = [334113513502430]

#times = [7, 15, 30]
#dists = [9,40,200]

x = np.arange(0,times[0])
x = np.where(x*(times[0]-x) > dists[0], 1, 0)

print(np.sum(x))