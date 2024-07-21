def solution(info, edges):
    visit = [0 for _ in range(len(info))]
    answer = []
    
    def dfs(sheep, wolf):
        if sheep > wolf:
            answer.append(sheep)  
        else:
            return

        for p, c in edges:
            if visit[p] and not visit[c]:
                visit[c] = 1
                if info[c] == 0:
                    dfs(sheep + 1, wolf)
                else:
                    dfs(sheep, wolf + 1)
                visit[c] = 0
    visit[0] = 1
    dfs(1, 0)
    
    return max(answer)
    

# 옆 노드 방문 처리 실패
# import collections

# def bfs(info, child):
#     que = collections.deque()
#     que.append([0, 1])
    
#     result = 1
    
#     while que:
#         cur_node, value = que.popleft()
#         if cur_node in child:
#             # hash's value should not be mutable (TypeError: unhashable type: 'list')
#             children = tuple(child[cur_node])
#             for i in range(len(children)):
#                 animal = info[children[i]]
#                 if animal == 0:
#                     value += 1
#                 else:
#                     value -= 1
                
#                 if value > 0:
#                     result = max(result, value)
#                     que.append([children, value])
                    
#     return result

# def solution(info, edges):
#     answer = 0
#     child = collections.defaultdict(list)
    
#     for edge in edges:
#         child[edge[0]].append(edge[1])

#     answer = bfs(info, child)
    
#     return answer