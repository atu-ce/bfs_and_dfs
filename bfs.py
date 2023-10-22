graphic = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'B'],
    'D': [],
    'E': ['A'],
    'F': [],
}

visitList = []
stackList = []

def BFS(visitList, graphic, node):
    stackList.append(node)

    while stackList:
        stack = stackList.pop(0)
        visitList.append(stack)

        for neighbour in graphic[stack]:
            if neighbour not in visitList:
                stackList.append(neighbour)

BFS(visitList, graphic, 'A')

print("DFS Ziyaret Sıralaması:", end=" ")
for visit in visitList:
    if visit is not visitList[-1]:
        print(visit, end=" -> ")
    else:
        print(visit)