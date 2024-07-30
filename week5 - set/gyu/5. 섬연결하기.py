def find(disjoitnset,i):
    if disjoitnset[i] == i:
        return i
    
    return find(disjoitnset, disjoitnset[i])

def union(disjointset, a, b):
    node1 = find(disjointset,a)
    node2 = find(disjointset,b)
    
    disjointset[node2] = node1

def is_cycle(disjointset, a, b):
    root1 = find(disjointset,a)
    root2 = find(disjointset,b)
    
    return root1 == root2

def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    answer = 0
    disjointset = [i for i in range(n)]
    
    for cost in costs:
        src = cost[0]
        dest = cost[1]
        
        if is_cycle(disjointset, src, dest):
            continue
        
        union(disjointset, src, dest)
        answer += cost[2]
        
    return answer