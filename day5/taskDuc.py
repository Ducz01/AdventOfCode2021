import numpy as np

with open('day5/inputDuc.txt') as f:
    lines = f.readlines()

maxSize = 1000
board = np.full((maxSize, maxSize), 0)
def part1():
    for line in lines:
        parts = line.split(' -> ')
        part1 = parts[0].split(',')
        part2 = parts[1].split(',')
        
        
        isVertical = part1[0] == part2[0]
        isHorizontal = int(part1[1]) == int(part2[1])
        if lines.index(line) == 485:
            print(part1)
            print(part2)
            print(isHorizontal)
        if (not isHorizontal) and (not isVertical):
            continue
        if isHorizontal:
            firstValue = int(part1[0])
            secondValue = int(part2[0])
            staticValue = int(part1[1])
            lower =0
            upper = 0
            if firstValue < secondValue:
                lower = firstValue
                upper = secondValue
            else:
                lower = secondValue
                upper = firstValue
            for i in range(lower, upper+1):
                
                current = board[i][staticValue]
                board[i][staticValue] = current+1
        if isVertical:
            firstValue = int(part1[1])
            secondValue = int(part2[1])
            staticValue = int(part2[0])
            lower =0
            upper = 0
            if firstValue < secondValue:
                lower = firstValue
                upper = secondValue
            else:
                lower = secondValue
                upper = firstValue

            for i in range(lower, upper+1):
                current = board[staticValue][i]
                board[staticValue][i] = current+1


    count = len(board[board>=2])
    print(count)

def part2():
    for line in lines:
        parts = line.split(' -> ')
        part1 = parts[0].split(',')
        part2 = parts[1].split(',')
        
        isVertical = part1[0] == part2[0]
        isHorizontal = int(part1[1]) == int(part2[1])
        isDiagonal = abs(int(part1[0]) - int(part2[0])) == abs(int(part1[1]) - int(part2[1]))

        if isHorizontal:
            firstValue = int(part1[0])
            secondValue = int(part2[0])
            staticValue = int(part1[1])
            lower =0
            upper = 0
            if firstValue < secondValue:
                lower = firstValue
                upper = secondValue
            else:
                lower = secondValue
                upper = firstValue
            for i in range(lower, upper+1):
                
                current = board[i][staticValue]
                board[i][staticValue] = current+1
        if isVertical:
            firstValue = int(part1[1])
            secondValue = int(part2[1])
            staticValue = int(part2[0])
            lower =0
            upper = 0
            if firstValue < secondValue:
                lower = firstValue
                upper = secondValue
            else:
                lower = secondValue
                upper = firstValue

            for i in range(lower, upper+1):
                current = board[staticValue][i]
                board[staticValue][i] = current+1

        if isDiagonal:
            xFirstValue = int(part1[0])
            xSecondValue = int(part2[0])
            yFirstValue = int(part1[1])
            ySecondValue = int(part2[1])
            xCountUp = True
            yCountUp = True
            if xFirstValue > xSecondValue:
                xCountUp = False
            if yFirstValue > ySecondValue:
                yCountUp = False
            length = abs(xFirstValue - xSecondValue)
            for i in range(length+1):
                if lines.index(line) == 494:
                    print(parts)
                    print(xFirstValue)
                    print(yFirstValue)
                current = board[xFirstValue][yFirstValue]
                board[xFirstValue][yFirstValue] = current+1

                if xCountUp:
                    xFirstValue = xSecondValue - (abs(xSecondValue - xFirstValue)-1)
                else:
                    xFirstValue = xSecondValue + (abs(xSecondValue - xFirstValue)-1)
                if yCountUp:
                    yFirstValue = ySecondValue - (abs(ySecondValue - yFirstValue)-1)
                else: 
                    yFirstValue = ySecondValue + (abs(ySecondValue - yFirstValue)-1)

    count = len(board[board>=2])
    print(count)

part2()