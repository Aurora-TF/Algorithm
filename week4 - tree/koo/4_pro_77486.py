def solution(enroll, referral, seller, amount):
    length = len(enroll)
    answer = [0] * length
    parent = {}
    key_index = {}
    
    for i in range(length):
        key_index[enroll[i]] = i
    
    for i in range(length):
        if referral[i] != '-':
            idx = enroll.index(referral[i])
            parent[enroll[i]] = idx
            
    for s in range(len(seller)):
        idx = key_index[seller[s]]
        money = amount[s] * 100
        option = money // 10
        
        answer[idx] += money - option
        
        while True:
            if enroll[idx] not in parent:
                break
            else:
                next_node = parent[enroll[idx]]
                
                money = option
                option = money // 10
                answer[next_node] += money - option
                idx = next_node
                
                if option == 0:
                    break

    return answer
