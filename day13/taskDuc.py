import matplotlib.pyplot as plt
import numpy as np

with open('day13/inputDuc.txt') as f:
    lines = f.readlines()
    f.close()

coordinates = []
print(lines[0])
instructions=[]
for line in lines:
    if ',' in line:
        cleanLine = line.strip()
        parts = cleanLine.split(',')
        coordinates.append((int(parts[0]),int(parts[1])))
    if 'fold' in line:
        cleanLine = line.strip()
        parts = cleanLine.split(' ')
        instructionvalues = parts[2].split('=')
        instructions.append((instructionvalues[0],instructionvalues[1]))

def fold(instruction, coordinates):
    (axis, semivalue) = instruction
    value = int(semivalue)
    for index, coordinate in enumerate(coordinates):
        (x,y) = coordinate
        if axis == 'x':
            if x > value:
                diff = x - value
                newpos = (value-diff, y)
                coordinates[index] = newpos
        if axis == 'y':
            if y > value:
                diff = y -value
                newpos = (x, value-diff)
                coordinates[index] = newpos
    return list(set(coordinates))

def part1():
    print(len(fold(instructions[0], coordinates)))
def part2():
    board = coordinates
    for instruction in instructions:
        board = fold(instruction, board)

    print(board)

    fig, ax = plt.subplots()
    for coord in board:
        (x,y) = coord 
        ax.plot([int(x)], [int(y)], 'bo')
    plt.show()


part2()

