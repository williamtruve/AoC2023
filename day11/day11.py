
import enum
import functools
import itertools
from operator import indexOf
import matplotlib.pyplot as plt
import more_itertools
from aocd import get_data, submit
from collections import Counter
import math
import networkx as nx
from pyparsing import col
from sympy import true
from tqdm import tqdm
import numpy as np
from utils.aocutils import get_neighbors
import multiprocessing


data = get_data(day=11, year=2023).splitlines()

data = open("day11/inp.txt", "r").readlines()
data = open("day11/test.txt", "r").readlines()

#Build matrix
#If row is only columns add row twice
#Transpose and add row, transpose back
empty_rows = []
matrix = []
for x, d in enumerate(data):
    rc = 0
    for r in d.strip():
        if r != ".":
            rc += 1
    if rc == 0:
        empty_rows.append(x)
    matrix.append(list(d.strip()))

matrix = np.array(matrix)
matrix = np.transpose(matrix)

newMatrix = []
empty_cols = []
for y, m in enumerate(matrix):
    rc = 0
    for r in m:
        if r != ".":
            rc += 1
    if rc == 0:
        empty_cols.append(y)
    newMatrix.append(m)

newMatrix = np.array(newMatrix)
matrix = np.transpose(newMatrix)
node_indices = [(u[0], u[1]) for u in np.argwhere(matrix == "#")]
node_pairs = more_itertools.distinct_combinations(node_indices, 2)
def manhattan(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))
 
def solve(adder, node_pairs):
    total_sum = 0
    adder = int(adder)
    for pair in tqdm(node_pairs):
        u, v = pair
        row_range = list(range(min(u[0], v[0])+1, max(u[0], v[0])))
        col_range = list(range(min(u[1], v[1])+1, max(u[1], v[1])))
        for yx in empty_rows:
            if yx in row_range:
                total_sum += (adder)-1
        for hx in empty_cols:
            if hx in col_range:
                total_sum += (adder)-1
        total_sum += manhattan(u ,v)
    return total_sum    
#print(solve(2, node_pairs))
print(solve(1000000, node_pairs))
