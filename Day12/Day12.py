file = open("input.txt", "r")
file = file.readlines()
dict = {}

for i in file:
    i = i[:-1]
    newLine = i.replace(',', '').split()
    #newLine = [s.replace('<->', '') for s in newLine]
    #newLine.pop(1)
    dict[newLine[0]] = newLine[2:]

visited = set()

def dfs(graph, node, visited):
    if node not in visited:
        visited.add(node)
        for x in graph[node]:
            dfs(graph, x, visited)

#dfs(dict, '0', visited)
#print(len(visited))

nrGroups = 0

for i in dict:
    if i not in visited:
        nrGroups += 1
        dfs(dict, i, visited)

print(nrGroups)