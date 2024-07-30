from collections import defaultdict, deque

def solution(graph, start):
    adj_list = defaultdict(list)

    for u, v in graph:
        adj_list[u].append(v)

    def bfs(start):
        visit = set()

        queue = deque([start])
        visit.add(start)
        result.append(start)

        while queue:
            node = queue.popleft()
            for neighbor in adj_list.get(node, []):
                if neighbor not in visit:
                    queue.append(neighbor)
                    visit.add(neighbor)
                    result.append(neighbor)

        result = []
        bfs(start)

        return result