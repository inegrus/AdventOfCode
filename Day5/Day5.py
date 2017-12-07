
file = open("input.txt", "r")
content = file.readlines()
content = [int(e.strip()) for e in content]

result = 0
max_jumps = len(content)
step = 0
index = 0

while index in range(0, max_jumps):
    step = content[index]
    if content[index] >= 3:
        content[index] -= 1
    else:
        content[index] += 1
    index += step
    result += 1

print(result)