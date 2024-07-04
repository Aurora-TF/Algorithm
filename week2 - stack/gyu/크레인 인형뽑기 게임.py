def grab(board,target):
    length = len(board)
    for j in range(length):
        if board[j][target] == 0:
            continue
        else:
            ret = board[j][target]
            board[j][target] = 0
            return ret
    return 0

def solution(board, moves):
    stack = []
    answer = 0

    for move in moves:
        ret = grab(board, move-1)
        if ret != 0:
            if stack and stack[-1] == ret:
                stack.pop()
                answer += 2
            else:
                stack.append(ret)

    return answer