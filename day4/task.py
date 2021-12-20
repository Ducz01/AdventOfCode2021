import numpy as np

with open('day4/inputDuc.txt') as f:
    lines = f.readlines()

#Save numbers to draw in array
drawString = lines[0]
drawPool = drawString.split(',')

#check if all valus in row are the same
def findRow(array):
    #convert to numpy array
    array = np.array(array)
    #for each row -> similar to len()
    for i in range(array.shape[0]):
        #if all values are the same return true
        if np.all(array[i]==-1):
            return True
    return False

#check if all valus in column are the same
def findColumn(array):
    #convert to numpy array
    array = np.array(array)
    #transpose matrix -> rows are columns now and vice versa
    array = array.T
    #for each row aka column
    for i in range(array.shape[0]):
        #if all values are the same return true
        if np.all(array[i] == -1):
            return True
    return False

#check if diagonal exists
def findDiagonal(array):
    #set to true
    diagonal = True
    #convert to numpy array
    array = np.array(array)
    #for each row 
    for i in range(array.shape[0]):
        #if diagonal value is not -1 set diagonal to false
        if array[i][i] != -1:
            diagonal = False
    #if not diagonal 
    if not diagonal:
        #set back to true
        diagonal = True
        #for each row 
        for i in range(array.shape[0]):
            #if diagonal value the other way is not -1 set diagonal to false
            if array[i][4-i] != -1:
                diagonal = False
    return diagonal

#empty list of boards
boards = []
#empty bord matrix 0 rows,5columns
board = np.empty((0, 5), int)

#for each line from line 2 til end
for i in range(2,len(lines),1):
    #if value mod 6 is one -> empty line -> board just finished
    if i % 6 == 1:
        #append finished board to list
        boards.append(board)
        #empty board
        board = np.empty((0, 5), int)
    
    #otherwise
    else:
        #save numbers of row
        row = [int(s) for s in lines[i].split() if s.isdigit()]
        #append list as array to board matrix
        board = np.append(board, np.array([row]), axis=0)
        
        #super stupid but if last line add board to boards
        if i == len(lines)-1:
            boards.append(board)
            board = np.empty((0, 5), int)


def part1():
    #won is false
    won = False
    #winning number default
    winningNumber = -1
    #empty winning board
    winningBoard = np.array
    #for each drawing number
    for number in drawPool:
        #if already won break
        if won:
            break
        #for each board
        for board in boards:
            #if number exists in board
            if int(number) in board:
                #check number -> set to -1
                np.place(board, board == int(number), -1)
            
            #check if full row, column, diagonal exists
                if findRow(board) or findColumn(board) or findDiagonal(board):
                    #set won to true
                    won = True
                    #save winning board
                    winningBoard = board
                    #save winning number
                    winningNumber = number
                    break

    #get all values that are not checked aka -1 and add together
    sum = winningBoard[winningBoard != -1].sum(axis=0)
    print(sum * int(winningNumber))
           
def part2():
    #empty winning board
    losingBoard = np.array
    losingnumber = -1
    #for each drawing number
    for number in drawPool:
        #for each board
        boardToRemove = -1
        for index,board in enumerate(boards):
            #if number exists in board
            if int(number) in board:
                #check number -> set to -1
                np.place(board, board == int(number), -1)
            
            #check if full row, column, diagonal exists
                if findRow(board) or findColumn(board) or findDiagonal(board):
                    boards.pop(index)
                    print('now')
                    losingnumber = number
                    if len(boards) == 1:
                        losingBoard = boards[0]
                        break
                    

    #get all values that are not checked aka -1 and add together
    sum = losingBoard[losingBoard != -1].sum(axis=0)
    print(sum * int(losingnumber))

part2()


        