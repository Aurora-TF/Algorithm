def dfs(n,graph, s,e):
    stack = []
    check = [False for _ in range(n+1)]
    stack.append(s)
    
    while stack:
        cur = stack.pop()
        check[cur] = True
        
        for next_node in graph[cur]:
            if (cur == s and next_node == e) or (cur == e and next_node == s):
                continue
            
            if check[next_node]:
                continue
            
            stack.append(next_node)
    
    ret = 0
    for node in check:
        if node:
            ret += 1
    
    return ret

def solution(n, wires):
    answer = 101
    graph = [[] for _ in range(n+1)]
    
    for wire in wires:
        s = wire[0]
        e = wire[1]
        graph[s].append(e)
        graph[e].append(s)
    
    for wire in wires:
        s = wire[0]
        e = wire[1]
        ret1 = dfs(n, graph, s, e)
        ret2 = dfs(n, graph, e, s)
        answer = min(answer, abs(ret1 - ret2))
        
    return answer