
file = open("input.txt", "r")
numbers = file.read()

sum = 0

for i in range(0, len(numbers) - 1):
    if numbers[i] == numbers[i+1]:
        sum += int(numbers[i])

if numbers[len(numbers) - 1] == numbers[0]:
    sum += int(numbers[0])

print(sum)