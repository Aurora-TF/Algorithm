from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)

def insert(tree, node, parent_idx):
    idx, x, y = node
    (px, py), left, right = tree[parent_idx]
    
    if px < x:
        if right != 0:
            insert(tree, node, right)
        else:
            tree[parent_idx][2] = idx
            tree[idx] = [(x, y), 0, 0]
    else:
        if left != 0:
            insert(tree, node, left)
        else:
            tree[parent_idx][1] = idx
            tree[idx] = [(x, y), 0, 0]
            
def pre_order(tree, node_idx):
    result = []
    
    if node_idx == 0:
        return result
    
    result.append(node_idx)
    result += pre_order(tree, tree[node_idx][1])
    result += pre_order(tree, tree[node_idx][2])
    
    return result

def post_order(tree, node_idx):
    result = []
    
    if node_idx == 0:
        return result
    
    result += post_order(tree, tree[node_idx][1])
    result += post_order(tree, tree[node_idx][2])
    result.append(node_idx)
    
    return result


def solution(nodeinfo):
    answer = [[]]
    node_with_idx = []
    tree = defaultdict(list)
    
    for idx, [x, y] in enumerate(nodeinfo, 1):
        node_with_idx.append([idx, x, y])
    node_with_idx.sort(key = lambda x: x[2])
    
    root_idx, rx, ry = node_with_idx.pop()
    tree[root_idx] = [(rx, ry), 0, 0]
    
    while node_with_idx:
        node = node_with_idx.pop()
        insert(tree, node, root_idx)
    
    answer = [pre_order(tree, root_idx), post_order(tree, root_idx)]
    
    return answer