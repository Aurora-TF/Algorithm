DON_KNOW = -1
DEFEAT = 1
WIN = 2
ME = 3

def dfs(n,graph,graph_map,start):
    check = [False for _ in range(n + 1)]
    stack = [start]
    
    while stack:
        cur = stack.pop()
        check[cur] = True
        
        for next_node in graph[cur]:
            if check[next_node]:
                continue
            graph_map[start][next_node] = WIN
            graph_map[next_node][start] = DEFEAT
            stack.append(next_node)

def solution(n, results):
    graph_map = [[DON_KNOW for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        graph_map[i][i] = ME
        
    graph = [[] for _ in range(n + 1)]
    
    for result in results:
        win = result[0]
        defeat = result[1]
        graph[win].append(defeat)
    
    for win in range(1, n + 1):
        dfs(n, graph, graph_map, win)
        
    answer = 0
    for row in graph_map[1:]:
        is_ans = True
        for col in row[1:]:
            if col == DON_KNOW:
                is_ans = False
                break
        if is_ans:
            answer += 1 
    
    return answer