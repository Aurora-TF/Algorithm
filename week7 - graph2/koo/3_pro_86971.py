from collections import deque, defaultdict

def bfs(n, start, graph):
    visit = [0] * (n + 1)
    que = deque([start])
    visit[start] = 1
    cnt = 1
    
    while que:
        node = que.popleft()
        for i in graph[node]:
            if not visit[i]:
                que.append(i)
                visit[i] = 1
                cnt += 1
    return cnt

def solution(n, wires):
    answer = n
    
    graph = defaultdict(list)
    
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        
        answer = min(abs(bfs(n, a, graph) - bfs(n, b, graph)), answer)
        
        graph[a].append(b)
        graph[b].append(a)
        
    return answer