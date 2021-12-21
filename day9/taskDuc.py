import numpy as np
import sys
sys.setrecursionlimit(10000)

with open('day9/inputDuc.txt') as file:
    lines=file.readlines()
    file.close()

rows = len(lines)
columns = len(lines[0].strip())
def checkNeighbours(board,coords):
    neighbourcount = 0
    i = coords[0]
    j = coords[1]
    neighbours = []
    value = board[i][j]

    isLeft = j <=0
    isRight = j>=columns-1
    isUp = i<=0
    isDown = i>=rows-1

    if isLeft and isUp:
        if board[i+1][j] > value and board[i+1][j] < 9:
            neighbours.append((i+1),j)
        if board[i][j+1] > value and board[i][j+1] < 9:
            neighbours.append((i,j+1))
    elif isLeft and isDown:
        if board[i][j+1] > value and board[i][j+1] < 9:
            neighbours.append((i,j+1))
        if board[i-1][j] > value and board[i-1][j] < 9:
            neighbours.append((i-1,j))
    elif isRight and isUp:
        if board[i+1][j] > value and board[i+1][j] < 9:
            neighbours.append((i+1,j))
        if board[i][j-1] > value and board[i][j-1] < 9:
            neighbours.append((i,j-1))
    elif isRight and isDown:
        if board[i][j-1] > value and board[i][j-1] < 9:
            neighbours.append((i,j-1))
        if board[i-1][j] > value and board[i-1][j] < 9:
            neighbours.append((i-1,j))
    elif isUp:
        if board[i+1][j] > value and board[i+1][j] < 9:
            neighbours.append((i+1,j))
        if board[i][j-1] > value and board[i][j-1] < 9:
            neighbours.append((i,j-1))
        if board[i][j+1] > value and board[i][j+1] < 9:
            neighbours.append((i,j+1))
    elif isRight:
        if board[i+1][j] > value and board[i+1][j] < 9:
            neighbours.append((i+1,j))
        if board[i][j-1] > value and board[i][j-1] < 9:
            neighbours.append((i,j-1))
        if board[i-1][j] > value and board[i-1][j] < 9:
            neighbours.append((i,j-1))
    elif isDown:
        if board[i][j-1] > value and board[i][j-1] < 9:
            neighbours.append((i,j-1))
        if board[i-1][j] > value and board[i-1][j] < 9:
            neighbours.append((i-1,j))
        if board[i][j+1] > value and board[i][j+1] < 9:
            neighbours.append((i,j+1))
    elif isLeft:
        if board[i-1][j] > value and board[i-1][j] < 9:
            neighbours.append((i-1,j))
        if board[i][j+1] > value and board[i][j+1] < 9:
            neighbours.append((i,j+1))
        if board[i+1][j] > value and board[i+1][j] < 9:
            neighbours.append((i+1,j))
    else:
        if board[i-1][j] > value and board[i-1][j] < 9:
            neighbours.append((i-1,j))
        if board[i][j+1] > value and board[i][j+1] < 9:
            neighbours.append((i,j+1))
        if board[i+1][j] > value and board[i+1][j] < 9:
            neighbours.append((i+1,j))
        if board[i][j-1] > value and board[i][j-1] < 9:
            neighbours.append((i,j-1))
    neighbourcount += len(neighbours)
    for neighbour in neighbours:
        neighbourcount += checkNeighbours(board, neighbour)
    print(neighbourcount)
    return neighbourcount



def part1():
    
    board = np.full((rows, columns), 9)
    for lineIndex,line in enumerate(lines):
        thisLine = line.strip()
        for charIndex,char in enumerate(thisLine):
            board[lineIndex][charIndex] = char
    print(board[0])

    lowPoints = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            value = board[i][j]
            leftIsBigger = False
            rightIsBigger = False
            upIsBigger = False
            downIsBigger = False

            isLeft = j <=0
            isRight = j>=columns-1
            isUp = i<=0
            isDown = i>=rows-1

            if isLeft and isUp:
                upIsBigger = True
                leftIsBigger = True
                if board[i+1][j] > value:
                    downIsBigger = True
                if board[i][j+1] > value:
                    rightIsBigger = True
            elif isLeft and isDown:
                leftIsBigger = True
                downIsBigger = True
                if board[i][j+1] > value:
                    rightIsBigger = True
                if board[i-1][j] > value:
                    upIsBigger = True
            elif isRight and isUp:
                rightIsBigger = True
                upIsBigger = True
                if board[i+1][j] > value:
                    downIsBigger = True
                if board[i][j-1] > value:
                    leftIsBigger = True
            elif isRight and isDown:
                rightIsBigger = True
                downIsBigger = True
                if board[i][j-1] > value:
                    leftIsBigger = True
                if board[i-1][j] > value:
                    upIsBigger = True
            elif isUp:
                upIsBigger = True
                if board[i+1][j] > value:
                    downIsBigger = True
                if board[i][j-1] > value:
                    leftIsBigger = True
                if board[i][j+1] > value:
                    rightIsBigger = True
            elif isRight:
                rightIsBigger = True
                if board[i+1][j] > value:
                    downIsBigger = True
                if board[i][j-1] > value:
                    leftIsBigger = True
                if board[i-1][j] > value:
                    upIsBigger = True
            elif isDown:
                downIsBigger = True
                if board[i][j-1] > value:
                    leftIsBigger = True
                if board[i-1][j] > value:
                    upIsBigger = True
                if board[i][j+1] > value:
                    rightIsBigger = True
            elif isLeft:
                leftIsBigger = True
                if board[i-1][j] > value:
                    upIsBigger = True
                if board[i][j+1] > value:
                    rightIsBigger = True
                if board[i+1][j] > value:
                    downIsBigger = True
            else:
                if board[i-1][j] > value:
                    upIsBigger = True
                if board[i][j+1] > value:
                    rightIsBigger = True
                if board[i+1][j] > value:
                    downIsBigger = True
                if board[i][j-1] > value:
                    leftIsBigger = True
            if upIsBigger and rightIsBigger and downIsBigger and leftIsBigger:
                lowPoints.append(value)
    print(lowPoints)
    sum = 0
    for point in lowPoints:
        sum+= (point+1)
    print(sum)

def part2():
    print('start part 2')
    rows = len(lines)
    columns = len(lines[0].strip())
    board = np.full((rows, columns), 9)
    for lineIndex,line in enumerate(lines):
        thisLine = line.strip()
        for charIndex,char in enumerate(thisLine):
            board[lineIndex][charIndex] = char

    lowPoints = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            value = board[i][j]
            leftIsBigger = False
            rightIsBigger = False
            upIsBigger = False
            downIsBigger = False

            isLeft = j <=0
            isRight = j>=columns-1
            isUp = i<=0
            isDown = i>=rows-1

            if isLeft and isUp:
                upIsBigger = True
                leftIsBigger = True
                if board[i+1][j] > value:
                    downIsBigger = True
                if board[i][j+1] > value:
                    rightIsBigger = True
            elif isLeft and isDown:
                leftIsBigger = True
                downIsBigger = True
                if board[i][j+1] > value:
                    rightIsBigger = True
                if board[i-1][j] > value:
                    upIsBigger = True
            elif isRight and isUp:
                rightIsBigger = True
                upIsBigger = True
                if board[i+1][j] > value:
                    downIsBigger = True
                if board[i][j-1] > value:
                    leftIsBigger = True
            elif isRight and isDown:
                rightIsBigger = True
                downIsBigger = True
                if board[i][j-1] > value:
                    leftIsBigger = True
                if board[i-1][j] > value:
                    upIsBigger = True
            elif isUp:
                upIsBigger = True
                if board[i+1][j] > value:
                    downIsBigger = True
                if board[i][j-1] > value:
                    leftIsBigger = True
                if board[i][j+1] > value:
                    rightIsBigger = True
            elif isRight:
                rightIsBigger = True
                if board[i+1][j] > value:
                    downIsBigger = True
                if board[i][j-1] > value:
                    leftIsBigger = True
                if board[i-1][j] > value:
                    upIsBigger = True
            elif isDown:
                downIsBigger = True
                if board[i][j-1] > value:
                    leftIsBigger = True
                if board[i-1][j] > value:
                    upIsBigger = True
                if board[i][j+1] > value:
                    rightIsBigger = True
            elif isLeft:
                leftIsBigger = True
                if board[i-1][j] > value:
                    upIsBigger = True
                if board[i][j+1] > value:
                    rightIsBigger = True
                if board[i+1][j] > value:
                    downIsBigger = True
            else:
                if board[i-1][j] > value:
                    upIsBigger = True
                if board[i][j+1] > value:
                    rightIsBigger = True
                if board[i+1][j] > value:
                    downIsBigger = True
                if board[i][j-1] > value:
                    leftIsBigger = True
            if upIsBigger and rightIsBigger and downIsBigger and leftIsBigger:
                lowPoints.append((i,j))
    result = 0
    print(result)
    for point in lowPoints:
        neighbourPoints = 0
        neighbourPoints += checkNeighbours(board, point)
        result += neighbourPoints
    print(result)


part2()