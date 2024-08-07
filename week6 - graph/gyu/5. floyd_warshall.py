# https://www.acmicpc.net/problem/11404
import sys

MAX_VALUE = 10**9

inputs = sys.stdin.readline
v = int(inputs()) + 1
e = int(inputs())

graph = [[MAX_VALUE] * v for _ in range(v)]

for _ in range(e):
    start, end, weight = map(int, inputs().split())
    graph[start][end] = min(graph[start][end], weight)

def floyd_warshall(v,graph):
    dist = [[MAX_VALUE] * v for _ in range(v)]
    
    for i in range(v):
        for j in range(v):
            if i == j:
                dist[i][j] = 0
                continue
            dist[i][j] = graph[i][j]
            
    for k in range(v):
        for i in range(v):
            for j in range(v):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                
    return dist

dist = floyd_warshall(v,graph)

for row in dist[1:]:
    for col in row[1:]:
        if col == MAX_VALUE:
            print(0, end=" ")
            continue    
        print(col, end=" ")
    print()