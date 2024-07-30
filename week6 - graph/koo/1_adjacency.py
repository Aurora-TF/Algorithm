# matrix
node, edge = map(int, input().split())

graph = [[] for j in range(node) for i in range(node)]

for _ in range(edge):
    startNode, endNode = map(int, input().split())
    graph[startNode][endNode] = 1
    graph[endNode][startNode] = 1

# list
node, edge = map(int, input().split())

graph = [[] for i in range(node)]

for _ in range(edge):
    startNode, endNode = map(int, input().split())
    graph[startNode].append(endNode)
    graph[endNode].append(startNode)