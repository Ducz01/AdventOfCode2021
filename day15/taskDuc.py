import numpy as np
from functools import cmp_to_key
import json

with open('day15/inputDuc.txt') as f:
    lines = [line.strip() for line in f.readlines()]

height = len(lines)
width = len(lines[0])
queue = []
board = np.full((height, width), 0)
boardValues = {}
for i in range(height):
    for j in range(width):
        board[i][j] = lines[i][j]
        queue.append((j,i))
        boardValues[(i,j)] = 9999999999
startpos = (0,0)
destination = (width-1, height-1)

def getAdjacents(node, prev):
    adj = []
    (x,y) = node
    if x > 0:
        adj.append((x-1,y))
    if x < width-1:
        adj.append((x+1,y))
    if y > 0:
        adj.append((x, y-1))
    if y < height-1:
        adj.append((x, y+1))
    filterdAdjacents = [adjpos for adjpos in adj if adjpos != prev]
    return filterdAdjacents

def compare(item1, item2):
    return boardValues[item1] - boardValues[item2]

boardValues[startpos] = 0
boardPredecessor = boardValues.copy()
boardPredecessor[startpos] = None
previous = startpos
print(board)
while len(queue) > 0:
    # Calling
    sorted(queue, key=cmp_to_key(compare))
    currentNode = queue[0]
    queue.pop(0)
    adjacents = getAdjacents(currentNode, previous)
    nextNodes = []
    for adj in adjacents:
        (x,y) = adj
        value = boardValues[currentNode] + board[y][x]
        if value < boardValues[adj]:
            boardValues[adj] = value
            boardPredecessor[adj] = currentNode
    previous = currentNode

path = []
currentEndpoint = (width-1, height-1)
#path.append(board[currentEndpoint[1]][currentEndpoint[0]])
path.append(currentEndpoint)

while currentEndpoint != None:
    predecessor = boardPredecessor[currentEndpoint]
    if predecessor == None:
        break
    (x,y) = predecessor
    path.append(predecessor)
    currentEndpoint = predecessor
path.reverse()

print(path)
print(boardValues)
print(boardValues[(width-1, height-1)])
for pos in path:
    print(pos, boardValues[pos])