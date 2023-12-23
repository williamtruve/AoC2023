from utils.aocutils import get_neighbors
import copy
import networkx as nx
from tqdm import tqdm
import numpy as np

data = open("day23/input.txt","r").readlines()
#data = open("day23/test.txt","r").readlines()

matrix = []
for d in data:
    matrix.append(list(d.strip()))

matrix = np.array(matrix)


### Start by finding all conjunction indices in the matrix
conjunctions = 0
checkif = set()
from collections import defaultdict
cons = defaultdict(int)
for rx in range(len(matrix)):
    for cx in range(len(matrix[0])):
        neighbors = get_neighbors(rx,cx, matrix)
        nsum = 0
        if matrix[rx,cx] != "#":
            for n in neighbors:
                if matrix[n] != "#":
                    nsum += 1
            if (nsum == 3) or nsum == 1 or nsum == 4:
                for n in neighbors:
                    checkif.add((rx,cx))
                conjunctions += 1

Gprim = nx.Graph()
distanceDict = defaultdict(int)
### Build the graph, From every conjunction, do BFS until you reach another conjunction, set that as an edge in the graph
for c in tqdm(checkif):
    pats = defaultdict(int)
    visited = [c]
    pos = c
    cost = 0
    solves = [(visited,pos, cost)]
    while solves:
        visited, pos, cost = solves.pop(0)
        for n in get_neighbors(pos[0], pos[1], matrix):
            if matrix[n] != "#":
                if n in checkif:
                    Gprim.add_edge(c, n, weight = cost+1)
                    Gprim.add_edge(n, c, weight = cost+1)
                else:
                    if n not in visited:
                        newVisits = copy.deepcopy([*visited, pos])
                        solves.append((newVisits, n, cost+1))

### Path finding made easy by nx :) 
start = (0,1)
goal = (len(matrix)-1, len(matrix[0])-2)
simple_paths = (nx.all_simple_paths(Gprim, start, goal))
longestHikeSteps = 0
longestHike= []
for path in tqdm(simple_paths):
    if nx.path_weight(Gprim, path, weight="weight") > longestHikeSteps:
        longestHikeSteps = nx.path_weight(Gprim, path, weight="weight")
        longestHike = path
print(longestHikeSteps)