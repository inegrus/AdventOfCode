def rellocation(line):
    valMax = max(line)
    indexMax = line.index(valMax) + 1
    line[indexMax - 1] = 0

    while(valMax > 0):
        if(indexMax == len(line)):
            indexMax = 0
        line[indexMax] += 1
        indexMax += 1
        valMax -= 1


file = open("input.txt", "r")
blocks = {}
steps = 0

line = file.readline().split()
line = list(map(int, line))
blocks[str(line)] = 0

while(True):
    rellocation(line)
    steps += 1
    if str(line) in blocks:
        print(steps - blocks[str(line)])
        break
    else:
        blocks[str(line)] = steps






