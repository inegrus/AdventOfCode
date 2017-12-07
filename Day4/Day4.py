from collections import Counter

file = open("input.txt", 'r')

lines = file.readlines()
notValid = answer = 0


for line in lines:
    cnt = Counter() # Tally occurrences of words in a list
    line = line[:-1] #without \n
    line = line.split() #modify line to be a list of strings and not a string

    for i in line:
        #i = ''.join(sorted(i))
        i = str(sorted(i))
        cnt[i] += 1
        if cnt[i] > 1:
            notValid += 1

    if notValid == 0:
        answer += 1
    else:
        notValid = 0

print(answer)