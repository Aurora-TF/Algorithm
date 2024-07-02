def solution(board, moves):
    answer = 0
    stack = []
    depth = len(board)
    
    for move in moves:
        move -= 1
        temp = 0
        
        for dep in range(depth):            
            temp = board[dep][move]
            
            if temp == 0:
                continue
            else:
                board[dep][move] = 0
                break
        
        if temp == 0:
            continue        
        elif len(stack) == 0:
            stack.append(temp)        
        elif stack[-1] == temp:
            stack.pop()
            answer += 2
        else:
            stack.append(temp)
                
    return answer