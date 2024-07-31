import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        cur_distance, cur_destination = heapq.heappop(queue)

        if distances[cur_destination] < cur_distance:
            continue
    
        for new_destination, new_distance in graph[cur_destination].items():
            distance = cur_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])

    return distances