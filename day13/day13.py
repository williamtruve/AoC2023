import itertools
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


data = get_data(day=13, year=2023)

#data = open("day13/test.txt", "r").read()


matrices = []

full_data = data.split("\n\n")
for data in full_data:
    matrix = []
    for d in data.split("\n"):
        matrix.append(list(d.strip()))
    matrices.append(np.array(matrix))

matchedidx = 0


def solverMa(matrix):
    kol_solutions = set()
    row_solutions = set()
    for rx in range(len(matrix[0])-1):
        if (matrix[:,rx] == matrix[:,rx+1]).all():
            x = 2
            matched = True
            while rx+x < len(matrix[0]) and rx-(x-1) >= 0:
                #print(rx, x, "kol")
                if not (matrix[:,rx-(x-1)] == matrix[:,rx+(x)]).all():  
                    matched = False
                    break
                x += 1

            if matched:
                matchedidx = rx+1
                kol_solutions.add(matchedidx)
                
        for cx in range(len(matrix)-1):
            #print(matrix[cx,:])
            #print(matrix[cx+1,:])
            if (matrix[cx,:] == matrix[cx+1,:]).all():
                matched = True
                x = 2
                while cx+x < len(matrix) and cx-(x-1) >= 0 :
                    #print(x, "row")
                    if not (matrix[cx-(x-1),:] == matrix[cx+x,:]).all():
                        matched = False
                        break

                    x +=1
                if matched:
                    matchedidx = cx+1
                    row_solutions.add(matchedidx)
    return row_solutions, kol_solutions

kol_sums = 0
row_sums = 0
for matrix in matrices:
    found = False
    matrix = np.where(matrix == "#", 0, 1)
    firstRowSol, firstKolSol = solverMa(matrix)
    secondRowSol = set()
    secondKolSol = set()
    for hx in range(len(matrix)):
        for wx in range(len(matrix[0])):
            matrix = np.where(matrix == "#", 0, 1)
            matrix[hx][wx] = (matrix[hx][wx] + 1) % 2
            srs, sks = solverMa(matrix)
            for ele in srs:
                secondRowSol.add(ele)
            for ele in sks:
                secondKolSol.add(ele)
            matrix[hx][wx] = (matrix[hx][wx] + 1) % 2
    kolSet = (secondKolSol-firstKolSol)
    if kolSet != set():
        kol_sums += list(kolSet)[0]
    rowSet = (secondRowSol-firstRowSol)
    if rowSet != set():
        row_sums += list(rowSet)[0]
print(kol_sums)
print(row_sums*100+kol_sums)