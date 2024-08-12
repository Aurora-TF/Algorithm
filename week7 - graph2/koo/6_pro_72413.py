import heapq
from collections import defaultdict

def solution(n, s, a, b, fares):
    inf = int(1e9)
    answer = inf
    graph = defaultdict(list)
    
    for fare in fares:
        node1, node2, fee = fare
        graph[node1].append((node2, fee))
        graph[node2].append((node1, fee))
        
    def dijkstra(s):
        heap = []
        distance = [inf] * (n + 1)
        heapq.heappush(heap, (0, s))
        
        distance[s] = 0
        
        while heap:
            dist, current = heapq.heappop(heap)
            
            if distance[current] < dist:
                continue
            
            for g in graph[current]:
                cost = dist + g[1]
                
                if cost < distance[g[0]]:
                    distance[g[0]] = cost
                    heapq.heappush(heap, (cost, g[0]))
        return distance
        
    distances = [[]] + [dijkstra(i) for i in range(1, n + 1)]
    
    for i in range(1, n + 1):
        answer = min(distances[s][i] + distances[i][a] + distances[i][b], answer)
    
    return answer