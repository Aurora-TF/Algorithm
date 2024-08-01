from typing import Optional, Callable

n = 5
vertex_list = [(0,3),(1,2), (2,3), (3,4), (2,4), (1,3)]

# n은 노드 수, vertex_list은 간선 연결로 (start , end), 무방향 그래프
Graph_t = Optional[list[list]]
Vertex_t = tuple[int, int]
def solution(func: Callable, n: int, vertex_list: list[Vertex_t]):
    graph: Graph_t = func(n, vertex_list)
    
    for row in graph:
        for col in row:
            print(col, end=" ")
        print()
    

def matrix_graph(n: int, vertex_list: list[tuple[int, int]]) -> Graph_t:
    graph = [[0 for i in range(n)] for _ in range(n)]
    
    for v in vertex_list:
        start, end = v
        graph[start][end] = 1
        graph[end][start] = 1
    
    return graph

"""
  0 1 2 3 4
-|---------
0|0 0 0 1 0 
1|0 0 1 1 0 
2|0 1 0 1 1 
3|1 1 1 0 1 
4|0 0 1 1 0 
"""
solution(matrix_graph, n, vertex_list)

def list_graph(n: int, vertex_list: list[Vertex_t]) -> Graph_t:
    graph = [[] for _ in range(n)]
    
    for vertex in vertex_list:
        start, end = vertex
        graph[start].append(end)
        graph[end].append(start)
    
    return graph

"""
0: 3 
1: 2 3 
2: 1 3 4 
3: 0 2 4 1 
4: 3 2 
"""
solution(list_graph, n, vertex_list)