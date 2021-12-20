import numpy as np

with open('day4/input.txt') as f:
    lines = f.readlines()

drawString = lines[0]
drawPool = drawString.split(',')

boards = []
board = np.empty((0, 5), int)

def findRow(array):
    array = np.array(array)
    for i in range(array.shape[0]):
        if np.all(array[i]==-1):
            return True
    return False

def findColumn(array):
    array = np.array(array)
    array = array.T
    for i in range(array.shape[0]):
        if np.all(array[i] == -1):
            return True
    return False

def findDiagonal(array):
    diagonal = True
    array = np.array(array)
    for i in range(array.shape[0]):
        if array[i][i] != -1:
            diagonal = False
    if not diagonal:
        diagonal = True
        for i in range(array.shape[0]):
            if array[i][4-i] != -1:
                diagonal = False
    return diagonal

for i in range(2,len(lines),1):
    if i % 6 == 1:
        boards.append(board)
        board = np.empty((0, 5), int)
      
    else:
        row = [int(s) for s in lines[i].split() if s.isdigit()]
        board = np.append(board, np.array([row]), axis=0)
        
        if i == len(lines)-1:
            boards.append(board)
            board = np.empty((0, 5), int)

won = False
winningNumber = -1
winningBoard = np.array

for number in drawPool:
    if won:
        break
    for board in boards:
        if int(number) in board:
            np.place(board, board == int(number), -1)
           
            if findRow(board) or findColumn(board) or findDiagonal(board):
                won = True
                winningBoard = board
                winningNumber = number
                break

sum = winningBoard[winningBoard != -1].sum(axis=0)
print(sum * int(winningNumber))
           





        