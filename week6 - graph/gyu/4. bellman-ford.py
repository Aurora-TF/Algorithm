# https://www.acmicpc.net/problem/11657

import sys

def bellman_ford(v, edges, start):
    dist = ["INF"] * v
    dist[start] = 0
    
    for _ in range(v - 1):
        for s, e, w in edges:
            if dist[s] == "INF":
                continue
            
            if dist[e] == "INF":
                dist[e] = dist[s] + w
            
            dist[e] = min(dist[s] + w, dist[e])
    
    for s, e, w in edges:
        if dist[s] == "INF":
            continue
        
        if dist[e] > dist[s] + w:
            return True, -1
    
    return False ,dist

inputs = sys.stdin.readline
v, e = map(int, inputs().split())

edges = []
for _ in range(e):
    start, end, weight = map(int, inputs().split())
    edges.append((start, end, weight))

is_infinite , dist = bellman_ford(v+1, edges, 1)
if is_infinite:
    print(dist)
else:
    for d in dist[2:]:
        if d == "INF":
            print(-1)
            continue
        print(d)
