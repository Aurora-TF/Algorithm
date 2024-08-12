def solution(numbers, target):
    global answer
    answer = 0
    result = 0
    
    def arith(result, order, numbers, target):
        global answer
        if order == len(numbers):
            if result == target:
                answer += 1
                return
            else:
                return
        else:
            result += numbers[order]
            arith(result, order + 1, numbers, target)
            result -= numbers[order]
            
            result -= numbers[order]
            arith(result, order + 1, numbers, target)
            result += numbers[order]
            
    arith(result, 0, numbers, target)
        
    return answer