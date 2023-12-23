import errno
import itertools
from operator import index
from re import X
from turtle import pos
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
        solutionMatrix = defaultdict(helper3)
        dirs = ["U", "R", "D", "L"]
        aDist = defaultdict(int)

        position = (0,1)      
        #State should be (dir, pos, reps) 
        solve1 = ("R", position, 1)
        solutionMatrix[solve1] = matrix[position]
        aDist[solve1] = solutionMatrix[solve1] + manhattan_distance(position, endNode)

        position = (1,0)      
        solve2 = ("D", position, 1)
        solutionMatrix[solve2] = matrix[position]
        aDist[solve2] = solutionMatrix[solve2] + manhattan_distance(position, endNode)


        solves = [solve1, solve2]
        sc = 0
        closed_list = []
        while solves:
            sc += 1
            print(sc, len(solves))
            minVal = 999999999
            minIndex = None
            minSolver = None
            for xx, s in enumerate(solves):
                if (solutionMatrix[s] + manhattan_distance(s[1], endNode)) <= minVal:
                    minVal = (solutionMatrix[s] + manhattan_distance(s[1], endNode))
                    minSolver = s
                    minIndex = xx
            closed_list.append(minSolver)
            tmpSolution = solves.pop(minIndex)
            ogDir = tmpSolution[0]
            dir = tmpSolution[0]
            indexOfDir = dirs.index(dir)
            position = tmpSolution[1]

            positionx, positiony = tmpSolution[1]
            reps = tmpSolution[2]
            stepx, stepy = step(dir)
            if position == endNode and reps >= 4:
                print(solutionMatrix[minSolver])
                sys.exit()

            indexOfDir = dirs.index(dir)
            positionx, positiony = position

            stepx, stepy = step(dir)
            if position == endNode:
                print(sc, "iterations")
                print(solutionMatrix[tmpSolution])
                sys.exit()

            if reps < 3 and (positionx + stepx) in range(0,len(matrix)) and (positiony + stepy) in range(0, len(matrix)):
                nextPos = (positionx + stepx, positiony + stepy)

                tmpSolve = (dir, nextPos, reps + 1)
                if solutionMatrix[tmpSolve] >= solutionMatrix[tmpSolution] + matrix[nextPos]:
                    solutionMatrix[tmpSolve] = solutionMatrix[tmpSolution] + matrix[nextPos]
                    aDist[tmpSolve] = solutionMatrix[tmpSolve] + manhattan_distance(nextPos, endNode)
                    if tmpSolve not in closed_list and solutionMatrix[tmpSolve] + manhattan_distance(nextPos, endNode) <= 1009:
                        solves.append(tmpSolve)

            #Turn left
            dir = dirs[(indexOfDir)-1]
            stepx, stepy = step(dir)
            if (positionx + stepx) in range(0,len(matrix)) and (positiony + stepy) in range(0, len(matrix)):
                nextPos = (positionx + stepx, positiony + stepy)              
                tmpSolve = (dir, nextPos, 1)
                if solutionMatrix[tmpSolve] >= solutionMatrix[tmpSolution] + matrix[nextPos]:
                    solutionMatrix[tmpSolve] = solutionMatrix[tmpSolution] + matrix[nextPos]
                    aDist[tmpSolve] = solutionMatrix[tmpSolve] + manhattan_distance(nextPos, endNode)
                    if tmpSolve not in closed_list and solutionMatrix[tmpSolve] + manhattan_distance(nextPos, endNode) <= 1009:
                        solves.append(tmpSolve)
            #Turn Right
            dir = dirs[((indexOfDir)+1) % 4]
            stepx, stepy = step(dir)
            if (positionx + stepx) in range(0,len(matrix)) and (positiony + stepy) in range(0, len(matrix)):
                nextPos = (positionx + stepx, positiony + stepy)
                tmpSolve = (dir, nextPos, 1)
                if solutionMatrix[tmpSolve] >= solutionMatrix[tmpSolution] + matrix[nextPos]:
                    solutionMatrix[tmpSolve] = solutionMatrix[tmpSolution] + matrix[nextPos]
                    aDist[tmpSolve] = solutionMatrix[tmpSolve] + manhattan_distance(nextPos, endNode)
                    if tmpSolve not in closed_list and solutionMatrix[tmpSolve]+ manhattan_distance(nextPos, endNode) <= 1009:
                        solves.append(tmpSolve)

def main():
    data = open("day17/input.txt", "r").read().splitlines()
    data = open("day17/test.txt", "r").read().splitlines()

    matrix = []

    for d in data:
        matrix.append(list(map(lambda x: int(x), d.strip())))
    matrix = np.array(matrix)
    endNode = (len(matrix)-1, len(matrix)-1)
    dijkstra(matrix, endNode)


if __name__ == '__main__':
    main()


