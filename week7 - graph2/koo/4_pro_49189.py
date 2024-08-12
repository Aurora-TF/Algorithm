from collections import defaultdict, deque

def solution(n, edge):
    answer = 0
    distance = [0] * (n + 1)
    
    diction = defaultdict(list)
    for first, second in edge:
        diction[first].append(second)
        diction[second].append(first)
        
    que = deque()
    que.append(1)
    distance[1] = 1
    
    while que:
        node = que.popleft()
        for new_node in diction[node]:
            if distance[new_node] == 0:
                que.append(new_node)
                distance[new_node] = distance[node] + 1
                
    max_num = max(distance)
    answer = distance.count(max_num)
    
    return answer