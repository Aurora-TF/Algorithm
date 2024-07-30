def find(disjointset, i):
    if disjointset[i] == i:
        return i
    
    return find(disjointset,disjointset[i])

def union(disjointset, first, second):
    root1 = disjointset[first]
    root2 = disjointset[second]
    
    disjointset[root2] = root1

def solution(k, operations):
    disjointset = [i for i in range(k)]
    for command in operations:
        if command[0] == 'u':
            first_node = command[1]
            second_node = command[2]
            union(disjointset, first_node, second_node)
        else:
            find_node = command[1]
            print("find:", find(disjointset,find_node))
    
    ans = 0 
    for i in range(len(disjointset)):
        if i == disjointset[i]:
            ans += 1
    
    return ans

print(solution(3,[['u', 0, 1], ['u', 1, 2], ['f', 2]]))
print(solution(4,[['u', 0, 1], ['u', 2, 3], ['f', 0]]))
print(solution(7, [
    ['u', 0, 2],
    ['u', 0, 1],
    ['u', 1, 3],
    ['u', 4, 5],
    ['u', 4, 6],
    ['f', 3],
    ['f', 5]
]))