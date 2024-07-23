'''
[[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
1. y로 정리해서 y값이 가장 큰 값이 맨 위의 값이다.
2. 해당 y값의 x값을 기준으로 x축왼쪽으로 가장 큰 값이면서 y값이 큰 값이 왼쪽 노드
3. 해당 y값의 x값을 기준으로 x축오른쪽으로 가장 작은 값이면서 y값이 큰 값이 오른쪽 노드이다.
4. y축으로 정리한 나머지에 대해서 도 똑같이 해준다.
'''
import sys
sys.setrecursionlimit(10**6)
from collections import deque, defaultdict

def preorder(graph, cur, ans):
    if cur and graph[cur]:
        ans.append(cur)
        if graph[cur][0]:
            preorder(graph, graph[cur][0], ans)
        if graph[cur][1]:
            preorder(graph, graph[cur][1], ans)

def postorder(graph, cur, ans):
    if cur and graph[cur]:
        if graph[cur][0]: 
            postorder(graph, graph[cur][0], ans)
        if graph[cur][1]:
            postorder(graph, graph[cur][1], ans)
        ans.append(cur)

def solution(nodeinfo: list):
    node_to_num = {}
    graph = defaultdict()

    for i in range(len(nodeinfo)):
        node_to_num[(nodeinfo[i][0], nodeinfo[i][1])] = i + 1

    nodeinfo.sort(key=lambda x: -x[1])

    q = deque()
    root_coor = (nodeinfo[0][0], nodeinfo[0][1])
    root = node_to_num[root_coor]
    q.append((root_coor, root, nodeinfo[1:]))

    while q:
        cur_coor, cur_num, cur_info = q.popleft()
        graph[cur_num] = [None, None]
        if not cur_info:
            continue

        left = []
        right = []
        for node in cur_info:
            if node[0] < cur_coor[0]: 
                left.append(node)
            else: 
                right.append(node)

        if left:
            left.sort(key=lambda x: (-x[1], -x[0]))
        if right:
            right.sort(key=lambda x: (-x[1], x[0]))
        
        if left:
            left_node = left[0]
            left_node = (left_node[0], left_node[1])
            left_num = node_to_num[left_node]
            graph[cur_num][0] = left_num
            q.append((left_node, left_num, left[1:]))
        if right:
            right_node = right[0]
            right_node = (right_node[0], right_node[1])
            right_num = node_to_num[right_node]
            graph[cur_num][1] = right_num
            q.append((right_node, right_num, right[1:]))
    
    ans1 = []
    preorder(graph, root, ans1)
    ans2 = []
    postorder(graph, root, ans2)
    answer = [ans1, ans2]
    return answer

print(solution(nodeinfo=[
    [5,3],
    [11,5],
    [13,3],
    [3,5],
    [6,1],
    [1,3],
    [8,6],
    [7,2],
    [2,2]]))

print(solution(nodeinfo=[
    [1,1],
    [2,2],
    [3,3]
    ]))

print(solution(nodeinfo=[
    [5,5],
    [1,10000]
    ]))

[[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]] 
[[7, 4, 6, 9, 1, 8, 5, 2, 3], [9, 6, 5, 8, 1, 4, 3, 2, 7]]