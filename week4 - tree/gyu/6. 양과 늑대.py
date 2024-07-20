from collections import deque, defaultdict

def bfs(info, graph,cur_node, s, w, next_nodes):
    q = deque()
    q.append((cur_node,0,0, next_nodes))
    max_s = 0
    while q:
        node, s, w, next_nodes = q.popleft()
        if info[node] == 0:
            s += 1
        elif info[node] == 1:
            w += 1

        if w >= s:
            continue

        max_s = max(max_s, s)
        
        for child in graph[node]:
            next_nodes.append(child)
        
        for next_node in next_nodes:
            new_next_nodes = next_nodes.copy()
            new_next_nodes.remove(next_node)
            q.append((next_node, s, w, new_next_nodes))

    return max_s

def solution(info, edges):
    graph = defaultdict(list)
    for edge in edges:
        s = edge[0]
        e = edge[1]
        graph[s].append(e)
    
    return bfs(info,graph, 0,0,0, [])
