graphic = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'B'],
    'D': [],
    'E': ['A'],
    'F': [],
}

visitList = []

def DFS(visitList, graphic, node):
    if node not in visitList:
        visitList.append(node)

        for neighbour in graphic[node]:
            DFS(visitList, graphic, neighbour)

DFS(visitList, graphic, 'A')

print("DFS Ziyaret Sıralaması:", end=" ")
for visit in visitList:
    if visit is not visitList[-1]:
        print(visit, end=" -> ")
    else:
        print(visit)