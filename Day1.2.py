
file = open("input.txt", "r")
numbers = file.read()

sum = 0
lg = len(numbers)
step = int(lg / 2)
index2 = 0

print(numbers[lg-1])
print(numbers[lg-2])
print(numbers[lg-3])

for index in range(0, lg):

    index2 = index + step

    if(index2 >= lg):
        index2 = index2-lg

    if(numbers[index] == numbers[index2]):
        sum += int(numbers[index])

print(sum)