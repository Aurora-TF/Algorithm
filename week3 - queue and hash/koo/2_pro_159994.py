def solution(cards1, cards2, goal):
    answer = 'Yes'
    
    for go in goal:
        if cards1 and cards1[0] == go:
            cards1.pop(0)
            continue
        elif cards2 and cards2[0] == go:
            cards2.pop(0)
            continue
        else:
            answer = 'No'
            break
    
    return answer