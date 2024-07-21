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
                    if cur.left:
                        cur = cur.left
                    else:
                        cur.left = Node(key)
                        break
                
                else:
                    if cur.right:
                        cur = cur.right
                    else:
                        cur.right = Node(key)
                        break
    
    def search(self, key):
        cur = self.root

        while cur and cur.val != key:
            if key < cur.val:
                cur = cur.left
            else:
                cur = cur.right
        return cur

def solution(lst, search_lst):
    bst = BST()
    for key in lst:
        bst.insert(key)
    result = []

    for search_val in search_lst:
        if bst.search(search_val):
            result.append(True)
        else:
            result.append(False)
    return result