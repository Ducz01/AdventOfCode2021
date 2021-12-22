import numpy as np

with open('day9/inputDuc.txt') as f:
    lines = f.readlines()
    f.close()
rows = len(lines)
columns = len(lines[0].strip())
board = np.full((columns, rows), 9)
def getAdjacentPoints(x,y):
    points=[]
    if x > 0:
        points.append((x-1,y))
    if x < columns-1:
        points.append((x+1, y))
    if y > 0:
        points.append((x,y-1))
    if y<rows-1:
        points.append((x,y+1))
    return points


for lineIndex,line in enumerate(lines):
    thisLine = line.strip()
    for charIndex,char in enumerate(thisLine):
        board[lineIndex][charIndex] = char
        
def part1():
    lowPoints = []

    print(board[0])
    for i in range(len(board)):
        for j in range(len(board[0])):
            value = board[i][j]
            adj = getAdjacentPoints(j,i)
            isLowest = True
            for neighbour in adj:
                if board[neighbour[1]][neighbour[0]] <= value:
                    isLowest = False
            if isLowest:
                if value == 9:
                    print(j,i)
                lowPoints.append(value)
    sum = 0
    for pointi in lowPoints:
        sum+=(pointi+1)

    print(sum)
