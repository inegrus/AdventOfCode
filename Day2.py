
file = open("input2.txt", "r")

lines = file.readlines()
sum = 0

for i in lines:
    i = i[:-1]
    newLine = i.split()
    newLine = list(map(int, newLine))
    for j in range(0, len(newLine)-1):
        for k in range(j+1, len(newLine)):
            if newLine[j] % newLine[k] == 0:
                sum += newLine[j] // newLine[k]
            if newLine[k] % newLine[j] == 0:
                sum += newLine[k] // newLine[j]
    # sum += max(newLine) - min(newLine)

print(sum)
