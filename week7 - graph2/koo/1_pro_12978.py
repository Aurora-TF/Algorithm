import heapq

def dijkstra(dist, adj):
    heap = []
    heapq.heappush(heap, [0, 1])
    
    while heap:
        di, node = heapq.heappop(heap)
        for d, n in adj[node] :
            if di + d < dist[n]:
                dist[n] = di + d
                heapq.heappush(heap, [di + d, n])

def solution(N, road, K):
    answer = 0
    inf = int(1e9)

    dist = [inf] * (N + 1)
    dist[1] = 0
    
    adj = [[] for _ in range(N + 1)]
    for r in road:
        adj[r[0]].append([r[2], r[1]])
        adj[r[1]].append([r[2], r[0]])
    
    dijkstra(dist, adj)
    
    for i in dist:
        if i <= K:
            answer += 1
    
    return answer


# 정렬로만 풀어보려고 시도했던 흔적
# def solution(N, road, K):
#     answer = 0
#     inf = int(1e9)
    
#     cluster = [inf] * (N + 1)
#     cluster[1] = 0
    
#     for i in range(len(road)):
#         if road[i][0] > road[i][1]:
#             road[i][0], road[i][1] = road[i][1], road[i][0]
    
#     road.sort()
    
#     for r in road:
#         start, end, distance = r
#         cluster[end] = min(cluster[start] + distance, cluster[end])
    
#     for i in range(1, N + 1):
#         if cluster[i] <= K:
#             answer += 1    

#     return answer