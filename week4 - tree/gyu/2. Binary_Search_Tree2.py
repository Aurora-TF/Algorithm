class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            cur = self.root
            while True:
                if key < cur.val:
                    if cur.left is None:
                        cur.left = Node(key)
                        break
                    else:
                        cur = cur.left
                elif key > cur.val:
                    if cur.right is None:
                        cur.right = Node(key)
                        break
                    else:
                        cur = cur.right

    def search(self, key):
        cur = self.root

        while cur and cur.val != key:
            if key < cur.val:
                cur = cur.left
            else:
                cur = cur.right
        
        return cur

def solution(nodes, find_list):
    bst = BST()

    for key in nodes:
        bst.insert(key)
    
    result = []
    for key in find_list:
        if bst.search(key):
            result.append(True)
        else:
            result.append(False)
    return result

print(solution([5, 3, 8, 4, 2, 1, 7, 10], [1, 2, 5, 6]))
print(solution([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))
# print(solution([5, 3, 8, 4, 2, 1, 7, 10], [1, 2, 5, 6])) # [True, True, True, False]
# print(solution([1, 3, 5, 7, 9], [2, 4, 6, 8, 10])) # [False, False, False, False, False] 