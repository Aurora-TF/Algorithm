"""
https://www.acmicpc.net/problem/1753

5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
"""
import sys
import heapq

inputs = sys.stdin.readline
n, m = map(int, inputs().split())
start = int(inputs())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, w = map(int, inputs().split())
    graph[s].append((w, e))

MAX = 987654321
def dijkstra(n, m, start,graph):
    dist = [MAX for _ in range(n + 1)]
    check = [False for _ in range(n + 1)]
    heap = [(0,start)]
    dist[start] = 0
    
    while heap:
        _, cur = heapq.heappop(heap)
        if check[cur]: 
            continue
        
        check[cur] = True
        
        for weight, node in graph[cur]:
            next_dist = weight + dist[cur]
            if next_dist < dist[node]:
                dist[node] = next_dist
            heapq.heappush(heap, (dist[node], node))
            
    for i in range(1, n+1):
        if dist[i] == MAX:
            print("INF")
        else:
            print(dist[i])

dijkstra(n, m, start, graph)