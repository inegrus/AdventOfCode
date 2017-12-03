#number = initialNumber = 12
number = 347990
initialNumber = 347991
square = 8
indexSquare = 2
numberCorner = 3

while(square < number):
    number -= square
    square += 8
    indexSquare += 1
    numberCorner += 2

indexSquare -= 1
numberCorner *= numberCorner
middleBottom = numberCorner - indexSquare
middleLeft = middleBottom - indexSquare * 2
middleTop = middleLeft - indexSquare * 2
middleRight = middleTop - indexSquare * 2

list = [middleBottom, middleLeft, middleTop, middleRight]
for i in range(0, 4):
    list[i] = abs(initialNumber - list[i])

nearValue = min(list)

print(square, indexSquare)
print("number corner:", numberCorner*numberCorner)
print("bottom:", middleBottom)
print("left:", middleLeft)
print("top:", middleTop)
print("right:", middleRight)
print("near value:", nearValue)
print("Number of steps:", indexSquare + nearValue)