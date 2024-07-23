PROFIT = 100

class Node:
    def __init__(self):
        self.parent = None
        self.profit = 0

def solution(enroll, referral, seller, amount):
    answer = []
    name_to_node = {}
    name_to_node["center"] = Node()

    for i in range(len(referral)):
        name = enroll[i]
        refer = referral[i]
        if refer == "-":
            refer = "center"

        node = Node()
        parent = name_to_node[refer]
        node.parent = parent
        name_to_node[name] = node

    for i in range(len(seller)):
        name = seller[i]
        profit = amount[i] * PROFIT
        node = name_to_node[name]
        
        while node and profit:
            value = profit // 10
            profit -= value
            node.profit += profit
            profit = value
            node = node.parent
        
    
    for name in enroll:
        node = name_to_node[name]
        answer.append(node.profit)
            
    return answer

amount = [12, 4, 2, 5, 10]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
print(solution(enroll=enroll, referral=referral, seller=seller, amount=amount))