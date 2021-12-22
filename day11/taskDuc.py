import numpy as np

with open('day11/inputDuc.txt') as f:
    lines = f.readlines()

height = len(lines)
width = len(lines[0])-1
board = np.full((height, width), 0)

for i in range(height):
    for j in range(width):
        board[i][j] = lines[i][j]

def filterAlreadyGlowed(adjacents, alreadyGlowed):
    notGlowed = []
    for adjacent in adjacents:
        if adjacent not in alreadyGlowed:
            notGlowed.append(adjacent)
    return notGlowed


def getAdjacent(position):
    adj = []
    (y,x) = position
    if y > 0:
        adj.append((y-1,x))
        if x > 0:
            adj.append((y-1, x-1))
        if x < width-1:
            adj.append((y-1, x+1))
    if y <height-1:
        adj.append((y+1,x))
        if x > 0:
            adj.append((y+1, x-1))
        if x < width-1:
            adj.append((y+1, x+1))
    if x > 0:
        adj.append((y,x-1))
    if x < width-1:
        adj.append((y, x+1))
    return adj
    
def glow(glowList):
    newGlows = []
    for y,x in glowList:
        board[y][x] = board[y][x] +1
        if board[y][x] >9:
            newGlows.append((y,x))
    return newGlows

def cleanUpGlow():
    for i in range(height):
        for j in range(width):
            if board[i][j] >9:
                board[i][j] = 0

def checkAllFlashed():
    for i in range(height):
        for j in range(width):
            if board[i][j] <= 9:
                return False
    return True

def performStep(counter):
    alreadyGlowed = []
    glowList = []
    for i in range(height):
        for j in range(width):
            board[i][j] = board[i][j] + 1
            if board[i][j] >9:
                glowList.append((i,j))
    while len(glowList) >0:
        adjacents = getAdjacent(glowList[0])
        alreadyGlowed.append(glowList[0])
        glowList.pop(0)
        toGlow = filterAlreadyGlowed(adjacents, alreadyGlowed)
        moreGlows = glow(toGlow)
        for pos in moreGlows:
            glowList.append(pos)
        newlist = list(dict.fromkeys(glowList))
        glowList = newlist
    if checkAllFlashed():
        print('all flashed at: ', counter+1)
    cleanUpGlow()
    return len(alreadyGlowed)





def part1():
    glowTimes = 0
    for i in range(500):
        glowTimes += performStep(i)
        #print(i,'------------------------')
        #print(board)
    print(glowTimes)




part1()