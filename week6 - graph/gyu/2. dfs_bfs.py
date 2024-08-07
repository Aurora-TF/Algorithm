"""
https://www.acmicpc.net/problem/1260

- input
4 5 1
1 2
1 3
1 4
2 4
3 4

- output
1 2 4 3
1 2 3 4
"""
n = 5

import sys
from collections import deque
inputs = sys.stdin.readline

n, v, start = map(int, inputs().split())
graph = [[] for _ in range(n + 1)]

for _ in range(v):
    s, e = map(int, inputs().split())
    graph[s].append(e)
    graph[e].append(s)

def dfs_stack(n, start, graph):
    visited = [False for _ in range(n + 1)]
    stack = [start]
    
    while stack:
        cur = stack.pop()
        if visited[cur]:
            continue
        
        print(cur, end=" ")
        visited[cur] = True
        
        for node in graph[cur]:
            stack.append(node)

def dfs_recursive(n, cur, visited, graph):
    visited[cur] = True
    print(cur, end=" ")
    for node in graph[cur]:
        if visited[node]:
            continue
        dfs_recursive(n, node, visited, graph)

def bfs(n, start, graph):
    visited = [False for _ in range(n+1)]
    q = deque()
    q.append(start)
    visited[start] = True
    
    while q:
        cur = q.popleft()
        print(cur, end=" ")
        for node in graph[cur]:
            if visited[node]:
                continue
            visited[node] = True
            q.append(node)

for node_list in graph:
    node_list.sort(key=lambda x: -x)

dfs_stack(n, start, graph)
"""
for node_list in graph:
    node_list.sort(key=lambda x: x)

visited = [False for _ in range(n + 1)]
dfs_recursive(n, start, visited, graph)
"""
print()
for node_list in graph:
    node_list.sort(key=lambda x: x)
    
bfs(n, start, graph)