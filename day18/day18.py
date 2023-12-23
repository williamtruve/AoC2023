import numpy as np
import numbers



def coordinateChange(direction: str):
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
def initMatrixSize(data):
    startPoisition = (0,0)
    currentX, currentY = startPoisition
    positions = []
    for d in data:
        direction, steps, color = (d.strip().split())
        steps = int(steps)
        xSteps, ySteps = coordinateChange(direction)
        currentX += xSteps*steps
        currentY += ySteps*steps
        positions.append((currentX, currentY))
    maxX = 0
    maxY = 0
    minX = 999
    minY = 999
    for x, y in positions:
        if x < minX:
            minX = x
        if y < minY:
            minY = y
        if x > maxX:
            maxX = x
        if y > maxY:
            maxY = y
    if minY < 0:
        maxY += abs(minY)
    if minX < 0:
        maxX += abs(minX)
    return np.ones((maxX+1, maxY+1), dtype=str), minY, minX
from shapely import Polygon

def main():
    data = open("day18/input.txt").readlines()
    #data = open("day18/test.txt").readlines()

    matrix, minY, minX = initMatrixSize(data)
    matrix = np.pad(matrix,10)
    startPosition = (0,0)
    currentX, currentY = startPosition
    path = [startPosition]
    x = int("deadbeef", 16)
    stepCount = 0
    for d in data:
        direction, steps, color = (d.strip().split())
        steps = int(color[2:7], 16)
        dir = color[-2]
        if dir == "0":
            dir = "R"
        elif dir == "1":
            dir = "D"
        elif dir == "2":
            dir = "L"
        else:
            dir = "U"
        direction = dir
        xSteps, ySteps = coordinateChange(direction)
        stepCount += steps
     #   for _ in range(steps):
        currentX += xSteps*steps
        currentY += ySteps*steps
            #matrix[currentX, currentY] = "#"
        path.append((currentX, currentY))

    #path = [(0,0), (0,1), (1,1), (1,0), (0,0)]
    polygon = Polygon(path)
    area = (polygon.area)
    print("Area", area)
    b = stepCount
    print("boundary points", b)
    i = area + 1 - (b)//2
    print("Internal points", i)
    print("answer", i+b)

if __name__ == "__main__":
    main()