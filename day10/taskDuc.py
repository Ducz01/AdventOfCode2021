with open('day10/inputDuc.txt') as f:
    lines = f.readlines()
    f.close()

tags = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}
def part1():
    errors = {
        ')': 0,
        ']': 0,
        '}': 0,
        '>': 0
    }

    scoresTable = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    errorScorePerLine = []
    for line in lines:
        thisLine = line.strip()
        progress = []
        for char in thisLine:
            
            if char in tags:
                progress.append(tags[char])
            else:
                if char == progress[len(progress)-1]:
                    progress.pop(len(progress)-1)
                else:
                    errors[char] = errors[char]+1
                    break
    score = 0
    for key,value in errors.items():
        print(key, value)
        score += scoresTable[key] * value
    errorScorePerLine.append(score)


    sum = 0
    for linescore in errorScorePerLine:
        sum += linescore
    print(sum)

def part2():
    scoresTable = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    completionScores=[]
    for line in lines:
        thisLine = line.strip()
        progress = []
        isBroken = False
        for char in thisLine:
            
            if char in tags:
                progress.append(tags[char])
            else:
                if char == progress[len(progress)-1]:
                    progress.pop(len(progress)-1)
                else:
                    isBroken = True
        if not isBroken:
            progress.reverse()
            lineScore = 0
            for tag in progress:
                lineScore *= 5
                lineScore += scoresTable[tag]
            completionScores.append(lineScore)
    completionScores.sort()
    print(completionScores)
    print(completionScores[int(len(completionScores)/2)])
                    
part2()