from utils.aocutils import Matrix
import sys

FILE = "day17/input.txt"
a = Matrix(FILE)
rows,cols = a.dims()
print(rows,cols)

class State:
    def __init__(self,r,c,d,h,i):
        self.r = r
        self.c = c
        self.d = d
        self.h = h
        self.i = i

    def distance(self,o):
        return abs(self.r-o.r)+abs(self.c-o.c)
    
    def __gt__(self, o): 
        sv = self.h + self.distance(GOAL)
        ov = o.h + o.distance(GOAL)
        return sv > ov

    def __eq__(self, o): 
        return s.r == o.r and s.c == o.c and s.d == o.d and s.i == o.i

from enum import Enum
class d(Enum):
    U = 1
    D = 2
    L = 3
    R = 4

GOAL = State(rows-1,cols-1,d.R,0,0)
STARTR = State(0,0,d.R,0,0)
STARTD = State(0,0,d.D,0,0)

def samepos(s1,s2):
    return s1.r == s2.r and s1.c == s2.c 

TURN = 3   
MSTEP = 10

def getnext(s):
    nxt = []
    match s.d:
        case d.R:
            if s.c < cols-1 and s.i < MSTEP:
                nxt.append(State(s.r,s.c+1,d.R,s.h+int(a.get(s.r,s.c+1)),s.i+1))
            if s.r > 0 and s.i > TURN:
                nxt.append(State(s.r-1,s.c,d.U,s.h+int(a.get(s.r-1,s.c)),1))
            if s.r < rows-1 and s.i > TURN:
                nxt.append(State(s.r+1,s.c,d.D,s.h+int(a.get(s.r+1,s.c)),1))
        case d.L:
            if s.c > 0 and s.i < MSTEP:
                nxt.append(State(s.r,s.c-1,d.L,s.h+int(a.get(s.r,s.c-1)),s.i+1))
            if s.r > 0 and s.i > TURN:
                nxt.append(State(s.r-1,s.c,d.U,s.h+int(a.get(s.r-1,s.c)),1))
            if s.r < rows-1 and s.i > TURN:
                nxt.append(State(s.r+1,s.c,d.D,s.h+int(a.get(s.r+1,s.c)),1))
        case d.U:
            if s.r > 0 and s.i < MSTEP:
                nxt.append(State(s.r-1,s.c,d.U,s.h+int(a.get(s.r-1,s.c)),s.i+1))
            if s.c > 0 and s.i > TURN:
                nxt.append(State(s.r,s.c-1,d.L,s.h+int(a.get(s.r,s.c-1)),1))
            if s.c < cols-1 and s.i > TURN:
                nxt.append(State(s.r,s.c+1,d.R,s.h+int(a.get(s.r,s.c+1)),1))
        case d.D:
            if s.r < rows-1 and s.i < MSTEP:
                nxt.append(State(s.r+1,s.c,d.D,s.h+int(a.get(s.r+1,s.c)),s.i+1))
            if s.c > 0 and s.i > TURN:
                nxt.append(State(s.r,s.c-1,d.L,s.h+int(a.get(s.r,s.c-1)),1))
            if s.c < cols-1 and s.i > TURN:
                nxt.append(State(s.r,s.c+1,d.R,s.h+int(a.get(s.r,s.c+1)),1))
    return nxt

def dirchar(d):
    match d:
        case d.U:
            return b'^'
        case d.D:
            return b'v'
        case d.L:
            return b'<'
        case d.R:
            return b'>'
        case _:
            print('huh')

def invisit(s):
    global visited
    if (s.r,s.c,s.d,s.i) in visited:
        return visited[(s.r,s.c,s.d,s.i)]
    else:
        return None

from queue import PriorityQueue
curr = PriorityQueue()
curr.put(STARTR)
curr.put(STARTD)

visited = {}
goals = []

while not curr.empty():
    x1 = curr.qsize()
    s = curr.get()
    if samepos(s,GOAL) and s.i >= 4:
        print(' GOAL',s.h,s.i,end=", ")
        goals.append(s.h)
        continue
    v = invisit(s)
    if v == None:
        visited[(s.r,s.c,s.d,s.i)] = s.h
        nxt = list(filter(lambda x:not invisit(x),getnext(s)))
        x2 = len(nxt)
        for n in nxt:
            curr.put(n)
        x3 = curr.qsize()
    else:
        if s.h < v:
            del visited[(s.r,s.c,s.d,s.i)]
            curr.put(s)

print('\ndone',min(goals))


# Correct part 1: 668 

# viktor.txt 1135

# Part 2 735 FEL!!!  725?  Viktors svar på mitt: 789

## Fel: 907, 926, 925, 897, 901, 883