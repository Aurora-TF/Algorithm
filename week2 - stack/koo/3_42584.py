def solution(prices):
    answer = [0 for _ in range(len(prices))]
    stack = []
    
    for i in range(len(prices)):
        if len(stack) != 0:
            while stack[-1][0] > prices[i]:
                answer[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
                
                if stack == []:
                    break
                    
            stack.append([prices[i], i])    
        else:
            stack.append([prices[i], i])
    
    while stack != []:
        answer[stack[-1][1]] = len(prices) - stack[-1][1] - 1
        stack.pop()
    
    return answer