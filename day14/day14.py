import itertools
from operator import index
from re import X
import more_itertools
from aocd import get_data, submit
from collections import Counter
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

def tilt_north(matrix) -> list:
    moves = 1
    while moves > 0:
        moves = 0
        for rowx in range(1, len((matrix))):
            for colx in range(len((matrix[0]))):
                element = matrix[rowx][colx]
                if element == "O" and matrix[rowx-1][colx] == ".":
                    matrix[rowx][colx] = "."
                    matrix[rowx-1][colx] = "O"
                    moves += 1
    return matrix

def tilt_south(matrix) -> list:
    moves = 1
    while moves > 0:
        moves = 0
        for rowx in range(len((matrix))-2, -1, -1):
            for colx in range(len((matrix[0]))):
                element = matrix[rowx][colx]
                if element == "O" and matrix[rowx+1][colx] == ".":
                    matrix[rowx][colx] = "."
                    matrix[rowx+1][colx] = "O"
                    moves += 1
    return matrix
def tilt_west(matrix) -> list:
    moves = 1
    while moves > 0:
        moves = 0
        for rowx in range(0, len((matrix))):
            for colx in range(1,len((matrix[0]))):
                element = matrix[rowx][colx]
                if element == "O" and matrix[rowx][colx-1] == ".":
                    matrix[rowx][colx] = "."
                    matrix[rowx][colx-1] = "O"
                    moves += 1
    return matrix

def tilt_east(matrix) -> list:
    moves = 1
    while moves > 0:
        moves = 0
        for rowx in range(0, len((matrix))):
            for colx in range(len((matrix[0]))-2,-1,-1):
                element = matrix[rowx][colx]
                if element == "O" and matrix[rowx][colx+1] == ".":
                    matrix[rowx][colx] = "."
                    matrix[rowx][colx+1] = "O"
                    moves += 1

    return matrix
def cycle(matrix):
    matrix = tilt_north(matrix)
    matrix = tilt_west(matrix)
    matrix = tilt_south(matrix)
    matrix = tilt_east(matrix)
    return matrix

def count_load(matrix) -> int:
    load = 0
    current_load = len(matrix)
    for rowx in range(len((matrix))):
        for colx in range(len((matrix[0]))):
            element = matrix[rowx][colx]
            if element == "O":
                load += current_load
        current_load -= 1
    return load


 
import copy
if __name__ == "__main__":
    data = open("day14/input.txt", "r").read().splitlines()

    #data = open("day14/test.txt", "r").read().splitlines()  
    matrix = []
    for d in data:
        d = d.strip()
        matrix.append(list(d))

    seen_matrices = []
    x = 1000000000
    for ix in (range(1, 220)):
        matrix_copy = copy.deepcopy(matrix)
        matrix = cycle(matrix)
        if matrix in seen_matrices:
            d = (ix - seen_matrices.index(matrix))
            x -= ix
            x = x % d
            for kx in range(x):
                matrix = cycle(matrix)
            break
        else:
            seen_matrices.append(matrix_copy)
    print(count_load(matrix))