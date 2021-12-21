with open('day8/inputDuc.txt') as f:
    lines = f.readlines()

def part1():
    matchinglengths = [2, 4,3,7]

    counter = 0
    for line in lines:
        thisline = line.strip()
        parts = thisline.split('|')
        outputs = parts[1].split(' ')
        print(outputs)
        for output in outputs:
            for length in matchinglengths:
                if len(output) == length:
                    counter += 1
                    continue
    print(counter)

"""
 000
1   2
1   2
1   2
 333
4   5
4   5
4   5
 666
"""

def part2():
    numberToSymbol = {
        '0': [0,1,2,4,5,6],
        '1': [2,5],
        '2': [0,2,3,4,6],
        '3': [0,2,3,5,6],
        '4': [1,2,3,5],
        '5': [0,1,3,5,6],
        '6': [0,1,3,4,5,6],
        '7': [0,2,5],
        '8': [0,1,2,3,4,5,6],
        '9': [0,1,2,3,5,6]
    }

    numberarr=[0,1,2,3,4,5,6,7,8,9]
    symbolToNumber={
        'a': numberarr,
        'b': numberarr,
        'c': numberarr,
        'd': numberarr,
        'e': numberarr,
        'f': numberarr,
        'g': numberarr,
    }
    for line in lines:
        parts = line.split('|')
        crypt = parts[0].split(' ')
part2()
