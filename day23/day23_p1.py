
data = open("day23/input.txt","r").readlines()

import networkx as nx
matrix = []

for d in data:
    matrix.append(list(d.strip()))
import numpy as np

matrix = np.array(matrix)


s = (0,1)
from utils.aocutils import get_neighbors
solutions = [(0,1,[(0,1)], 0)]
goalsReached = set()
iterations = 0
while solutions:
    if (iterations % 10000) == 0:
        print("Iteration: ", iterations)
    iterations += 1
    #print(solutions)

    rx, cx, path, steps = solutions.pop(0)
    neighburs = get_neighbors(rx, cx, matrix)
    #print(rx, cx, path, steps)
    nowhereToGo = True
    
    for n in neighburs:
        if matrix[n] in ["v", ">", "."]:
            if not n in path:
                #print((n[0], n[1], [*path, tuple(n)], steps+1))
                nowhereToGo = False
                if matrix[n] == ">":
                    if not (n[0], n[1]+1) in path:
                    #print((n[0], n[1]+1, [*path, tuple(n)], steps+1))
                        solutions.append((n[0], n[1]+1, [*path, (n[0],n[1]+1)], steps+2))
                elif matrix[n] == "v":
                    if not (n[0]+1, n[1]) in path:
                        solutions.append((n[0]+1, n[1], [*path, (n[0]+1,n[1])], steps+2))
                    #print((n[0]+1, n[1], [*path, tuple(n)], steps+1))
                else:
                    solutions.append((n[0], n[1], [*path, (n[0],n[1])], steps+1))

    
    if nowhereToGo and (rx == len(matrix)-1) and (cx == len(matrix[0])-2):
        goalsReached.add(steps)
print(goalsReached)
print(max(list(goalsReached)))

