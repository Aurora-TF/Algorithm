import heapq

MAX = 500000 + 1
def dijkstra(N, start, graph):
    dist = [MAX] * (N + 1)
    check = [False] * (N + 1)
    
    dist[start] = 0
    heap = [(0, start)]
    
    while heap:
        _, cur = heapq.heappop(heap)
        if check[cur]:
            continue
        
        check[cur] = True
        
        for next_node in graph[cur]:
            weight, end = next_node
            dist[end] = min(dist[end], dist[cur] + weight)
            heapq.heappush(heap, (dist[end], end))
            
    return dist

def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range(N + 1)] # graph = [[]] * (N + 1)  이건 하면 안된다. list가 복사된다. 
    
    for s, e ,w in road:
        graph[s].append((w,e))
        graph[e].append((w,s))
    
    dist = dijkstra(N, 1, graph)
    for d in dist:
        if d != MAX  and d <= K:
            answer += 1
    
    return answer