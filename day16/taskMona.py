with open('inputMona.txt') as f:
    lines = f.readlines()
    f.close()
binarycode = []
binaryvalues = {
    "0" : "0000",
    "1" : "0001",
    "2" : "0010",
    "3" : "0011",
    "4" : "0100",
    "5" : "0101",
    "6" : "0110",
    "7" : "0111",
    "8" : "1000",
    "9" : "1001",
    "A" : "1010",
    "B" : "1011",
    "C" : "1100",
    "D" : "1101",
    "E" : "1110",
    "F" : "1111"
}
for line in lines:
    for char in line:
       binarycode.append(binaryvalues[char])

def getVersionNumber(binaryString):
    versionbinary = "0"

    for char in range(3):
        versionbinary += binarycode[char]
        binarycode.pop(char)

    version = list(binaryvalues.keys())[list(binaryvalues.values()).index(versionbinary)]

    versionIDbinary = "0"

    for char in range(3):
        versionIDbinary += binarycode[char]
        binarycode.pop(char)

    versionID = list(binaryvalues.keys())[list(binaryvalues.values()).index(versionIDbinary)]

    if int(versionID) == 4:
        literalvalue = ""
        while binarycode[0] != 1:
            binarycode.pop(0)

            for char in range(4):
                literalvalue += binarycode[int(char)]
                binarycode.pop(char)
            binarycode.pop(0)
            for char in range(4):
                literalvalue += binarycode[int(char)]
                binarycode.pop(char)

    else:
        if binarycode[0] == 0:
            binarycode.pop(0)
        else:
            binNumbOfPacketes =""
            binarycode.pop(0)
            for char in range(7):
                binarycode.pop(char)
            for char in range(4):
                binNumbOfPacketes += binarycode[char]
                binarycode.pop(char)
            numbOfPackets = list(binaryvalues.keys())[list(binaryvalues.values()).index(binNumbOfPacketes)]

            for i in range(int(numbOfPackets)):
                for char in range(7):
                    binarycode.pop(char)
                for char in range(4):
                    binNumbOfPacketes += binarycode[char]
                    binarycode.pop(char)





