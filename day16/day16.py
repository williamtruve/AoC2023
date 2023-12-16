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
from sympy import true
from tqdm import tqdm
import numpy as np
import regex as re
from utils.aocutils import get_neighbors
import multiprocessing
import functools
from collections import defaultdict
from tail_recursive import tail_recursive



def nextDirection(currentDirection,row, col, grid):
    symbol = grid[row][col]
    directions = []
    if currentDirection == "right":
        if symbol == "|":
            directions.append("up")
            directions.append("down")
        elif symbol == "/":
            directions.append("up")
        elif symbol == "\\":
            directions.append("down")
        else:
            directions.append("right")

    elif currentDirection == "down":
        if symbol == "-":
            directions.append("left")
            directions.append("right")
        elif symbol == "/":
            directions.append("left")
        elif symbol == "\\":
            directions.append("right")
        else:
            directions.append("down")

    if currentDirection == "left":
        if symbol == "|":
            directions.append("up")
            directions.append("down")
        elif symbol == "/":
            directions.append("down")
        elif symbol == "\\":
            directions.append("up")
        else:
            directions.append("left")

    if currentDirection == "up":
        if symbol == "-":
            directions.append("left")
            directions.append("right")
        elif symbol == "/":
            directions.append("right")
        elif symbol == "\\":
            directions.append("left")
        else:
            directions.append("up")
    return directions
    
def getNextPos(direction: str) -> tuple:
    if direction == "right":
        return (0, 1)
    elif direction == "left":
        return (0, -1)
    elif direction == "up":
        return (-1, 0)
    elif direction == "down":
        return(1, 0)
    else:
        raise Exception(f"no valid direction found for direction {direction}")

data = open("day16/input.txt", "r").read().splitlines()
#data = open("day16/test.txt", "r").read().splitlines()
matrix = []
for d in data:
    matrix.append(list(d.strip()))
    
def opposites(directional: str):

    if directional == "right":
        return "left"
    elif directional == "left":
        return "right"
    elif directional == "up":
        return "down"
    else: 
        return "up"

traversed = []

def keepOnMoving(direction, currentPosition):
    if ((currentPosition, direction) in traversed):
        return [], currentPosition
    traversed.append((currentPosition, direction))
    deltaX, deltaY = getNextPos(direction)
    currentX, currentY = currentPosition
    if (currentX + deltaX >= 0 and currentX + deltaX < len(matrix)) and (currentY + deltaY >= 0 and currentY + deltaY < len(matrix[0])):
        currentX += deltaX
        currentY += deltaY
        nextDirs = nextDirection(direction, currentX, currentY, matrix)
        return nextDirs, (currentX, currentY)
    else:
        return [], currentPosition

if __name__ == "__main__":
    maxVal = 0
    directionStarts = ["right", "left", "up", "down"]
    col0 = []
    colLast = []
    for ix in range(len(matrix[0])):
        col0.append((("up"),(0, ix)))
        col0.append((("down"),(0, ix)))

        colLast.append((("up"),(len(matrix)-1, ix)))
        colLast.append((("down"),(len(matrix)-1, ix)))
 
    row0 = []
    rowLast = []
    for ix in range(len(matrix)):
        row0.append((("right"),(ix, 0)))
        row0.append((("left"),(ix, 0)))

        rowLast.append((("right"),(ix, len(matrix[0])-1)))
        rowLast.append((("left"),(ix, len(matrix[0])-1)))

    allStarts = [*colLast, *rowLast, *col0, *row0]

    for direrx, posit in tqdm(allStarts):
        rx, cx = posit
        direrx = nextDirection(direrx, rx, cx, matrix)
        currentPosition = (rx, cx)
        solutionsList = []
        #nextDirections, currentPosition = keepOnMoving(direrx, currentPosition)
        for dirri in direrx:
            solutionsList.append((dirri, currentPosition))
        while solutionsList:
            dire, pos = solutionsList.pop()
            nextDirections, currentPosition = keepOnMoving(dire, pos)
            for di in nextDirections:
                solutionsList.append((di, currentPosition))
        traversed = set(traversed)
        setet = set()
        for x, y in traversed:
            setet.add(x)
        
        if len(setet) > maxVal:
            maxVal = len(setet)
        traversed = []
    print(maxVal)