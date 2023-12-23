from sre_compile import dis
import numpy as np
import matplotlib.pyplot as plt
import copy
data = open("day22/input.txt", "r").readlines()
#data = open("day22/test.txt", "r").readlines()
import string
alphabet = list(string.ascii_uppercase)
#bricks = np.array()
maxX = 0
maxY = 0
maxZ = 0
bricks = {}
for bx, line in enumerate(data):
    
    line = line.strip()
    start, end = line.split("~")
    x,y,z = start.split(",")
    if int(x) > maxX:
        maxX = int(x)
    if int(y) > maxY:
        maxY = int(y)
    if int(z) > maxZ:
        maxZ = int(z)
    x,y,z = end.split(",")
    if int(x) > maxX:
        maxX = int(x)
    if int(y) > maxY:
        maxY = int(y)
    if int(z) > maxZ:
        maxZ = int(z)
    ranges = []
    for coords in zip(start.split(","), end.split(",")):
        x0, x1 = map(int, coords)
        smX = min(x0, x1)
        bigX = max(x0, x1)

        ranges.append([smX, bigX])
    bricks[bx] = copy.deepcopy(ranges)


matrix = np.zeros((maxX+1, maxY+1, maxZ+1))

matrix = np.where(matrix == 0, -1, 0)
for k, v in bricks.items():
    x0, x1 = v[0]
    y0, y1 = v[1]
    z0, z1 = v[2]
    for x in range(x0,x1+1):
        for y in range(y0, y1+1):
            for z in range(z0, z1+1):
                matrix[x,y,z] = k
moved = 1
movx = 0
while moved > 0:
    moved = 0
    if movx % 100 == 0:
        print("movx", movx)
    movx += 1
    for ix in range(len(bricks)):
        indices = np.argwhere(matrix == ix)
        canFall = True
        for ind in indices:
            x,y,z = ind
            #print(x,y,z)
            if (matrix[x,y,z-1] != -1 and matrix[x,y,z-1] != ix) or (z-1) < 1:
                canFall = False
        if (canFall) and (indices.size > 0):
            moved += 1
            matrix = np.where(matrix == ix, -1, matrix)
            for ind in indices:
                x1,y1,z1 = ind
                z1 = z1-1
                matrix[x1,y1,z1] = ix

originalX = matrix[:,0,:]
#for ix in range(3):
 #   print(np.transpose(matrix[:,ix,:]))


#print(matrix[:,0,:])
#print(matrix[0,:,:])


def fall(brickix, matrix) -> int:
    matrixC = copy.deepcopy(matrix)
    moved = 0
    matrixC = np.where(matrixC == brickix, -1, matrixC)
    for ix in range(len(bricks)):
        indices = np.argwhere(matrixC == ix)
        canFall = True
        for ind in indices:
            x,y,z = ind
            #print(x,y,z)
            if (matrixC[x,y,z-1] != -1 and matrixC[x,y,z-1] != ix) or (z-1) < 1:
                canFall = False
        if (canFall) and (indices.size > 0):
            moved += 1
            matrixC = np.where(matrixC == ix, -1, matrixC)
            for ind in indices:
                x1,y1,z1 = ind
                z1 = z1-1
                matrixC[x1,y1,z1] = ix
    if moved > 0:
        return 0
    else:
        return 1

disintegrate = 0
for bix in range(len(bricks)):
    print(bix)
    #print(bix, fall(bix, matrix))
    disintegrate += fall(bix, matrix)
print(disintegrate)