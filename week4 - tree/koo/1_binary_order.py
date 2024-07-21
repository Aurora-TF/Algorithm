def preorder(nodes, idx):
    result = []
    if idx < len(nodes):
        result.append(nodes[idx])
        result += preorder(nodes, idx * 2 + 1)
        result += preorder(nodes, idx * 2 + 2)
        return result
    else:
        return result

def inorder(nodes, idx):
    result = []
    if idx < len(nodes):
        result += inorder(nodes, idx * 2 + 1)
        result.append(nodes[idx])
        result += inorder(nodes, idx * 2 + 2)
        return result
    else:
        return result
    
def postorder(nodes, idx):
    result = []
    if idx < len(nodes):
        result += postorder(nodes, idx * 2 + 1)
        result += postorder(nodes, idx * 2 + 2)
        result.append(nodes[idx])
        return result
    else:
        return result

def solution(nodes):
    answer = [preorder(nodes, 0), inorder(nodes, 0), postorder(nodes, 0)]
    return answer