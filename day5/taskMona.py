import numpy as np

with open('day5/inputMona.txt') as f:
    lines = f.readlines()

def partOne():
    #list of coordinate pair matrix
    values = []
    #empty coordinate matrix
    coordinates = np.empty((0, 2), int)
    #max x value
    maxX = 0
    #max y value
    maxY = 0

    #for each line
    for line in lines:
        #split string into 3 parts
        valueHolder = line.split(' ')
        #save first coordinate pair
        value1 = [int(s) for s in valueHolder[0].split(',')]
        #save second coordinate pair
        value2 = [int(s) for s in valueHolder[2].split(',')]
        #append pairs to coordinate matrix
        coordinates = np.append(coordinates, np.array([value1,value2]), axis=0)
        #append coordinates to values
        values.append(coordinates)
    
        #check if new max value is found
        if coordinates[0][0] > maxX:
            maxX = coordinates[0][0]
        if coordinates[1][0] > maxX:
            maxX = coordinates[1][0]
        if coordinates[0][1] > maxY:
            maxY = coordinates[0][1]
        if coordinates[1][1] > maxY:
            maxY = coordinates[0][1] 
        
        #empty coordinates
        coordinates = np.empty((0, 2), int)


    #create a matrix, default values 0 and size of max values found
    map = np.full((maxY, maxX), 0)

    #for each value
    for value in values:
        #save x coords
        x1 = value[0][0]
        x2 = value[1][0]
        
        #save y coords
        y1 = value[0][1]
        y2 = value[1][1]

        #if x values are the same
        if x1 == x2: 
            #if y2 bigger than y1 switch values
            if y2 < y1:
                holder = y1
                y1 = y2
                y2 = holder
            
            #for each value between y coordinates add one to map value
            for i in range(y1,y2+1):
                map[i][x1] += 1

        #if y values are the same
        if  y1 == y2:
            #if x2 bigger than x1 switch values
            if x2 < x1:
                holder = x1
                x1 = x2
                x2 = holder
            #for each value between x coordinates add one to map value
            for i in range(x1,x2+1):
                map[y1][i] += 1

    #add up the sum         
    sum = map[map >= 2]
    print(len(sum))

def partTwo():
    #list of coordinate pair matrix
    values = []
    #empty coordinate matrix
    coordinates = np.empty((0, 2), int)
    #max x value
    maxX = 0
    #max y value
    maxY = 0

    #for each line
    for line in lines:
        #split string into 3 parts
        valueHolder = line.split(' ')
        #save first coordinate pair
        value1 = [int(s) for s in valueHolder[0].split(',')]
        #save second coordinate pair
        value2 = [int(s) for s in valueHolder[2].split(',')]
        #append pairs to coordinate matrix
        coordinates = np.append(coordinates, np.array([value1,value2]), axis=0)
        #append coordinates to values
        values.append(coordinates)
    
        #check if new max value is found
        if coordinates[0][0] > maxX:
            maxX = coordinates[0][0]
        if coordinates[1][0] > maxX:
            maxX = coordinates[1][0]
        if coordinates[0][1] > maxY:
            maxY = coordinates[0][1]
        if coordinates[1][1] > maxY:
            maxY = coordinates[0][1] 
        
        #empty coordinates
        coordinates = np.empty((0, 2), int)


    #create a matrix, default values 0 and size of max values found
    map = np.full((maxY+1, maxX+1), 0)

    #for each value
    for value in values:
        #save x coords
        x1 = value[0][0]
        x2 = value[1][0]
        
        #save y coords
        y1 = value[0][1]
        y2 = value[1][1]


        #if x values are the same
        if x1 == x2: 
            #if y2 bigger than y1 switch values
            if y2 < y1:
                    holder = y1
                    y1 = y2
                    y2 = holder
            #for each value between y coordinates add one to map value
            for i in range(y1,y2+1):
                map[i][x1] += 1

        #if y values are the same
        elif y1 == y2:
            #if x2 bigger than x1 switch values
            if x2 < x1:
                    holder = x1
                    x1 = x2
                    x2 = holder
            #for each value between x coordinates add one to map value
            for i in range(x1,x2+1):
                map[y1][i] += 1
        
        else:
            coordRange = abs(x1 - x2)
            for i in range(coordRange + 1):
                if x1 > x2:
                    if y1 > y2:
                        map[y1-i][x1-i] += 1 
                    else:
                        map[y1+i][x1-i] += 1
                else:
                    if y1 > y2:
                        map[y1-i][x1+i] += 1
                    else:
                        map[y1+i][x1+i] += 1
        
                 
    #add up the sum         
    sum = map[map >= 2]
    print(len(sum))

partTwo()
    