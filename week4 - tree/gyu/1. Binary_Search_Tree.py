def preorder(nodes, cur):
    if cur < len(nodes) and nodes[cur] is not None:
        ret = ""
        ret += str(nodes[cur]) + " "
        ret += preorder(nodes, cur*2 + 1)
        ret += preorder(nodes, cur*2 + 2)
        return ret
    else:
        return ""

def inorder(nodes, cur):
    if cur < len(nodes) and nodes[cur] is not None:
        ret = ""
        ret += inorder(nodes, cur*2 + 1)
        ret += str(nodes[cur]) + " "
        ret += inorder(nodes, cur*2 + 2)
        return ret
    else:
        return ""

def postorder(nodes, cur):
    if cur < len(nodes) and nodes[cur] is not None:
        ret = ""
        ret += postorder(nodes, cur*2 + 1)
        ret += postorder(nodes, cur*2 + 2)
        ret += str(nodes[cur]) + " "
        return ret
    else:
        return ""


def solution(nodes):
    return [
        preorder(nodes, 0)[:-1],
        inorder(nodes, 0)[:-1],
        postorder(nodes, 0)[:-1]
    ]

print(solution([1,2,3,4,5,6,7])) # ['1 2 4 5 3 6 7', '4 2 5 1 6 3 7', '4 5 2 6 7 3 1']
print(solution([1,4,8,3,5,None,7,2,None,None,None,None,None,6])) # ['1 4 3 2 5 8 7 6', '2 3 4 5 1 8 6 7', '2 3 5 4 6 7 8 1']