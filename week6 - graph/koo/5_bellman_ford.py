def solution(graph, source):
    num_vertices = len(graph)

    distance = [float("inf")] * num_vertices
    distance[source] = 0

    predecessor = [None] * num_vertices

    for temp in range(num_vertices - 1):
        for u in range(num_vertices):
            for v, weight in graph[u]:
                if distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight
                    predecessor[v] = u
            
    for u in range(num_vertices):
        for v, weight in graph[u]:
            if distance[u] + weight < distance[v]:
                return [-1]
            
    return [distance, predecessor]