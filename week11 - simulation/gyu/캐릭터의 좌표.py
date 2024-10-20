def solution(keyinput, board):
    answer = [0,0]
    w = board[0] // 2
    h = board[1] // 2
    for key in keyinput:
        if key == "left" and -w < answer[0]:
            answer[0] -= 1  
        elif key == "right" and answer[0] < w :
            answer[0] += 1
        elif key == "up" and answer[1] < h:
            answer[1] += 1
        elif key == "down" and -h < answer[1]:
            answer[1] -= 1
    return answer