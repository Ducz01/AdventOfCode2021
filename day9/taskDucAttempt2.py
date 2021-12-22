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

def filterPoints(points, value, queue):
    basinPoints=[]
    for point in points:
        if board[point[1]][point[0]] <9 and board[point[1]][point[0]]>value and point not in queue:
            basinPoints.append(point)
    return basinPoints


def part2():
    lowPoints = []

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
                lowPoints.append((j,i))
   
    basins = []
    for lowpoint in lowPoints:
        sum = 0
        basinsmember=[lowpoint]
        queue = [lowpoint]
        while len(queue)!=0:
            point = queue[0]
            sum+=1
            basinsmember.append(point)
            queue.remove(queue[0])
            neighbours = getAdjacentPoints(point[0],point[1])
            filteredNeighbours = filterPoints(neighbours, board[point[1]][point[0]], queue)
            for neigh in filteredNeighbours:
                queue.append(neigh)
        if lowPoints.index(lowpoint) == 0:
            print(lowpoint)
            print(sum)
            print(basinsmember)
        newlist = list(dict.fromkeys(basinsmember))
        basins.append(len(newlist))

    basins.sort(reverse=True)
    print(basins[0] * basins[1] * basins[2])
part2()