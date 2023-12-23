import errno
import itertools
from operator import index
from re import X
import more_itertools
from aocd import get_data, submit
from collections import Counter, deque
import math
import networkx as nx
from pyparsing import col
from sympy import EX, false, true
from tqdm import tqdm
import numpy as np
import regex as re
from utils.aocutils import get_neighbors
import multiprocessing
import functools
from collections import defaultdict
from tail_recursive import tail_recursive
from utils.aocutils import get_neighbors
from queue import PriorityQueue
def helper3():
    return 99999999

def helper2():
    return defaultdict(helper3)

def helper():
    return defaultdict(helper2)
def step(direction):
    if direction == "U":
        return (-1,0)
    elif direction == "R":
        return (0,1)
    elif direction == "D":
        return (1,0)
    elif direction == "L":
        return (0, -1)
    else:
        raise Exception("error")

@functools.cache
def manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

import sys
def dijkstra(matrix, endNode):
        solutionMatrix = defaultdict(helper)
        dirs = ["U", "R", "D", "L"]
        position = (0,0)       
        for d in dirs:
            position = (0,0)       
            solutionMatrix[position][d][1] = 0

            position = (0,1)       
            solutionMatrix[position][d][1] = matrix[position]

            position = (1,0)      
            solutionMatrix[position][d][1] = matrix[position]


        position = (0,1)       
        solve1 = {"dir":"R", "pos": position, "reps": 1}

        position = (1,0)      
        solve2 = {"dir":"D", "pos": position, "reps": 1}
        
        solves = [solve1, solve2]
        sc = 0
        closed_list = []
        while solves:
            print(sc)
            sc += 1
            minVal = 999999999
            minIndex = None
            minSolver = None
            for xx, s in enumerate(solves):
                if (solutionMatrix[s["pos"]][s["dir"]][s["reps"]] + manhattan_distance(s["pos"], endNode)) <= minVal:
                    minVal = (solutionMatrix[s["pos"]][s["dir"]][s["reps"]] + manhattan_distance(s["pos"], endNode))
                    minSolver = s
                    minIndex = xx
            closed_list.append(minSolver)
            tmpSolution = solves.pop(minIndex)
            ogDir = tmpSolution["dir"]
            dir = tmpSolution["dir"]
            indexOfDir = dirs.index(dir)
            position = tmpSolution["pos"]

            positionx, positiony = tmpSolution["pos"]
            reps = tmpSolution["reps"]
            stepx, stepy = step(dir)
            if position == endNode and reps >= 4:
                print(solutionMatrix[position][dir][reps])
                sys.exit()

            if reps < 10 and (positionx + stepx) in range(0,len(matrix)) and (positiony + stepy) in range(0, len(matrix)):
                nextPos = (positionx + stepx, positiony + stepy)

                tmpSolve = {"dir":dir, "pos": nextPos, "reps": reps + 1}
                if solutionMatrix[nextPos][dir][reps+1] >= solutionMatrix[position][dir][reps] + matrix[nextPos]:
                    solutionMatrix[nextPos][dir][reps+1] = solutionMatrix[position][dir][reps] + matrix[nextPos]
                    solves.append(tmpSolve)
            #Turn left
            dir = dirs[(indexOfDir)-1]
            stepx, stepy = step(dir)
            if reps > 3 and (positionx + stepx) in range(0,len(matrix)) and (positiony + stepy) in range(0, len(matrix)):
                nextPos = (positionx + stepx, positiony + stepy)              
                tmpSolve = {"dir":dir, "pos": nextPos, "reps": 1}
                if solutionMatrix[nextPos][dir][1] >= solutionMatrix[position][ogDir][reps] + matrix[nextPos]:
                    solutionMatrix[nextPos][dir][1] = solutionMatrix[position][ogDir][reps] + matrix[nextPos]
                    if tmpSolve not in closed_list:
                        solves.append(tmpSolve)
            #Turn Right
            dir = dirs[((indexOfDir)+1) % 4]
            stepx, stepy = step(dir)
            if reps > 3 and (positionx + stepx) in range(0,len(matrix)) and (positiony + stepy) in range(0, len(matrix)):
                nextPos = (positionx + stepx, positiony + stepy)
                tmpSolve = {"dir":dir, "pos": nextPos, "reps": 1}
                if solutionMatrix[nextPos][dir][1] >= solutionMatrix[position][ogDir][reps] + matrix[nextPos]:
                    solutionMatrix[nextPos][dir][1] = solutionMatrix[position][ogDir][reps] + matrix[nextPos]
                    if tmpSolve not in closed_list:
                        solves.append(tmpSolve)

def main():
    data = open("day17/input.txt", "r").read().splitlines()
    #data = open("day17/test.txt", "r").read().splitlines()

    matrix = []

    for d in data:
        matrix.append(list(map(lambda x: int(x), d.strip())))
    matrix = np.array(matrix)
    endNode = (len(matrix)-1, len(matrix)-1)
    dijkstra(matrix, endNode)


if __name__ == '__main__':
    main()


