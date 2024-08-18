MAX = 100000 * 200 * 200
def solution(n, s, a, b, fares):
    graph = [[MAX] * (n+1) for _ in range(n+1)]
    dist = [[0] * (n+1) for _ in range(n+1)]
    for fare in fares:
        start = fare[0]
        end = fare[1]
        fee = fare[2]
        graph[start][end] = fee
        graph[end][start] = fee
        
    for i in range(1, n + 1):
        for j in range(1 , n +1):
            if i == j:
                continue
            dist[i][j] = graph[i][j]
    
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                dist[i][j] = min(dist[i][k] + dist[k][j], dist[i][j])
    
    answer = MAX
    for i in range(1,n+1):
        answer = min(answer,dist[s][i] + dist[i][a] + dist[i][b])

    return answer