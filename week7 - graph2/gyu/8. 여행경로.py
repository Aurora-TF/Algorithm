from collections import defaultdict

# 약간 문제가 이상하다?? 그럼 이게 맞나?
# [["ICN", "SFO"], ["ICN", "ATL"], ["ICN", "GYU"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
# ["ICN", "SFO", "ATL", "ICN", "ATL", "SFO", "GYU"]
def dfs(graph, start):
    stack = []
    
    stack.append(start)
    ans = []
    
    while stack:
        cur = stack[-1]
            
        if len(graph[cur]) == 0:
            ans.append(cur)
            stack.pop()
            continue
        
        stack.append(graph[cur][0])
        graph[cur] = graph[cur][1:]

    return ans

def solution(tickets):
    graph = defaultdict(list)
        
    for ticket in tickets:
        s = ticket[0]
        e = ticket[1]
        
        graph[s].append(e)
    
    for node in graph:
        graph[node].sort()

    return dfs(graph, "ICN")[::-1]