from collections import deque

def solution(want, number, discount):
    q = deque()
    count = {}
    criteria = {}
    for item, num in zip(want, number):
        count[item] = 0
        criteria[item] = num
    
    answer = 0
    for item in discount:
        if len(q) < 10:
            q.append(item)
            if item not in count:
                count[item] = 0
                
            count[item] = count[item] + 1
            
        if len(q) == 10:
            is_find = True
            for key in criteria:
                if count[key] < criteria[key]:
                    is_find = False
                    break
            if is_find:
                answer += 1
            
            k = q.popleft()
            count[k] -= 1

    return answer