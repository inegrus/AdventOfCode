import numpy

number = 347991
edgLg = 11

matrix = numpy.zeros((edgLg, edgLg), dtype=numpy.int)
global i, j
i = edgLg // 2
j = i
matrix[i][j] = 1
current_length = 1

def compute_value(i, j):
    result = 0
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            result += matrix[x][y]
    return result

def execute_steps(addi, addj, nr):
    global i, j
    while nr > 0:
        i += addi
        j += addj
        matrix[i][j] = compute_value(i, j)
        if matrix[i][j] > number:
            print(matrix[i][j])
            exit()
        nr -= 1
steps = 5
while steps:
    current_length += 2
    execute_steps(0, 1, 1) # step right
    execute_steps(-1, 0, current_length - 2) # step up
    execute_steps(0, -1, current_length - 1) # step left
    execute_steps(1, 0, current_length - 1) # step down
    execute_steps(0, 1, current_length - 1) # step right
    steps -= 1
    print(matrix)