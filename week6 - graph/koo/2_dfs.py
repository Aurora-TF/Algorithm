graph = dict()
 
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

# stack
def dfs_stack(graph, start_node):
    need_visit = []
    visit = []

    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop()

        if node not in visit:
            visit.append(node)

            need_visit.extend(graph[node])
    
    return visit

# recursive
def dfs_recursive(graph, start, visit = []):
    visit.append(start)

    for node in graph[start]:
        if node not in visit:
            dfs_recursive(graph, node, visit)
    
    return visit