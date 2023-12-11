
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

data1 = open("day11/inp.txt", "r").readlines()
data = open("day11/test.txt", "r").readlines()

matrix = []
for d in data:
    rc = 0
    for r in d.strip():
        if r != ".":
            rc += 1
    if rc == 0:
        matrix.append(list(d.strip()))
    matrix.append(list(d.strip()))

matrix = np.array(matrix)

print(matrix)
G = nx.DiGraph()
node_indices = []
for rx, row in enumerate(matrix):
    for cx, column in enumerate(row):
        if matrix[rx][cx]== "#":
            neighbours = get_neighbors(rx, cx, matrix) #Indices
            for n in neighbours:
                r, c = n
                G.add_edge((rx,cx), (r,c))
            node_indices.append((rx, cx))
        else:
            neighbours = get_neighbors(rx, cx, matrix) #Indices
            for n in neighbours:
                r, c = n
                G.add_edge((rx,cx), (r,c))



node_pairs = more_itertools.distinct_combinations(node_indices, 2)
def manhattan(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))
 
total_sum = 0
for pair in tqdm(node_pairs):
    u, v = pair
    total_sum += manhattan(u ,v) + 1
print(total_sum)



