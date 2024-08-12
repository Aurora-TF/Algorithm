from collections import deque

def bfs(n, graph, start):
    check = [0 for _ in range(n + 1)]
    q = deque()
    q.append(start)
    check[start] = 1
    max_value = 0
    
    while q:
        cur = q.popleft()
        
        for next_node in graph[cur]:
            if check[next_node]:
                continue
            q.append(next_node)
            check[next_node] = check[cur] + 1
            max_value = max(max_value, check[next_node])
            
    ret = 0
    for node in range(1, n + 1):
        if check[node] == max_value:
            ret += 1
    
    return ret

def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    for e in edge:
        start = e[0]
        end = e[1]
        graph[start].append(end)
        graph[end].append(start)

    return bfs(n, graph, 1)