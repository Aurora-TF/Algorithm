from collections import Counter 

# 배열을 나눠서 매번 set를 만드는건 n 이 소요되므로 n^2 임 -> 시간초과
def solution(topping):
    answer = 0
    old = Counter(topping)
    young = set()
    
    for i in topping:
        old[i] -= 1
        young.add(i)
        
        if old[i] == 0:
            old.pop(i)
        if len(old) == len(young):
            answer += 1
    
    return answer