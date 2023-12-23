from termios import IXANY
from networkx import neighbors
from regex import F
from utils.aocutils import get_neighbors
from tqdm import tqdm
import numpy.polynomial.polynomial as poly

data = open("day21/input.txt","r").readlines()
#data = open("day21/test.txt","r").readlines()
import copy
import numpy as np
import sys
import matplotlib.pyplot as plt
import time
import more_itertools
#25, 69, 113, 157
all_sums = []
all_iters = []
for x in [5]:
    matrix = []
    for d in data:
        matrix.append(list(d.strip()))
    matrix = np.array(matrix)
    lm = len(matrix)
    rows = len(matrix)*x
    columns = len(matrix[0])*x
    newarray = np.empty((rows, columns),dtype=str)
    originS = np.argwhere(matrix == "S")[0]
    for rx in range(rows):
        for cx in range(columns):
            newarray[rx,cx] = matrix[rx % (rows // x),cx % (columns // x)]

    SSet = ((np.argwhere(newarray == "S")))

    SSet = set([(s[0], s[1]) for s in SSet])
    matrix = newarray

    print(len(matrix[0]))
    print(len(matrix))
    sums = []
    origin = [originS[0]+(lm*(x//2)),originS[1]+(lm*(x//2))]
    spreaders = [[originS[0]+(lm*(x//2)),originS[1]+(lm*(x//2))]]
    foundS = set()
    fondS = set()
    breaker = False
    for ix in tqdm((range(2000))):
        matrix = np.where(matrix == "O", ".", matrix)
        for sp in spreaders:
            rc, cx = sp
            neighbours = get_neighbors(sp[0], sp[1], matrix)
            for n in neighbours:
                if matrix[n] == "S":
                    if n not in fondS:
                        fondS.add(n)
                        foundS.add((n,ix+1))
                    if (SSet - fondS) == set():
                        all_iters.append(ix)
                        print(origin)
                        breaker = True
                        break
                if matrix[n] != "#":
                    matrix[n] = "O"
            if breaker:
                break
        if breaker:
            break

        # Display the initial matrix as an image

        spreaders = np.argwhere(matrix == "O")
        fmatrix = np.where(matrix == "O", 1, 0)
        fmatrix = np.where(matrix == "O", 1, 0)
        all_sums.append(np.sum(fmatrix))

        if ((ix+1)-64) % 131 in [-1, 0, 1]:
            print(ix+1)


            print(np.sum(fmatrix))
            fig, ax = plt.subplots()
            im = ax.imshow(fmatrix, cmap='viridis')
            im.set_array(fmatrix)
            plt.show()
            time.sleep(0.01)
            plt.close()

print(all_iters)
print(list(more_itertools.difference(all_iters, initial=0)))
foundS = list(foundS)
foundS.sort()
print(foundS)
foundRows = []
rowser = []
tmpRows = []
for f, ix in foundS:
    if f[0] in foundRows:
        tmpRows.append(ix)
    else:
        foundRows.append(f[0])
        rowser.append(tmpRows)
        tmpRows = []
        tmpRows.append(ix)
    print(ix)
rowser.append(tmpRows)
for r in rowser:
    print(r)
#print(list(more_itertools.difference(all_sums, initial=0)))
print()
print(26501365 % 131)
print(26501365 // 131)

#7265 295 Y eg odd
#7325 294 X eg even
x = [65, 196, 327]
y = [3691, 32975, 91439]
coefs = poly.polyfit(x, y, 4)
ffit = poly.polyval(x_new, coefs)
plt.plot(x_new, ffit)
# Y   X   Y   X   Y
# 1, 10, 18, 26, 34

#202301 full gardens to the left and right and up and down
