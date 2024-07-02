def solution(prices):
    length = len(prices)
    answer = [0] * length 

    stack = []
    for i in range(length):
        while stack and stack[-1][0] > prices[i]:
            item = stack.pop()
            answer[item[1]] = i - item[1] 
        stack.append((prices[i], i))
    
    while stack:
        item = stack.pop()
        answer[item[1]] = length - item[1] -1 

    return answer