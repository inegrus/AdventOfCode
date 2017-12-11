
file = open("input.txt", "r")

file = file.readlines()
myDict = {}
maxVal = -100

for line in file:
    line = line[:-1]
    line = line.split()

    if line[0] not in myDict:
        myDict[line[0]] = 0

    if line[4] not in myDict:
        myDict[line[4]] = 0

    condition = str(myDict[line[4]]) + line[5] + line[6]
    if eval(condition):
        if line[1] == 'inc':
            myDict[line[0]] += int(line[2])
        else:
            myDict[line[0]] -= int(line[2])

        if (maxVal < myDict[line[0]]):
            maxVal = myDict[line[0]]

#print(myDict[max(myDict, key = myDict.get)])
print(maxVal)