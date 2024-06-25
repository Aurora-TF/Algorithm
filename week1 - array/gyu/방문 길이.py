def solution(dirs):
    U = [[False] * 11 for _ in range(11)]
    D = [[False] * 11 for _ in range(11)]
    L = [[False] * 11 for _ in range(11)]
    R = [[False] * 11 for _ in range(11)]
    
    cur_y = 5
    cur_x = 5

    answer = 0
    for dir in dirs:
        if dir == 'U':
            if cur_y - 1 < 0:
                continue 
            if U[cur_y][cur_x] == False and D[cur_y-1][cur_x] == False:
                answer += 1
            
            U[cur_y][cur_x] = True
            cur_y = cur_y -1
        elif dir == 'D':
            if cur_y + 1 > 10:
                continue 
            if D[cur_y][cur_x] == False and U[cur_y+1][cur_x] == False:
                answer += 1
            
            D[cur_y][cur_x] = True
            cur_y = cur_y + 1
        elif dir == 'L':
            if cur_x - 1 < 0:
                continue 
            if L[cur_y][cur_x] == False and R[cur_y][cur_x-1] == False:
                answer += 1
            
            L[cur_y][cur_x] = True
            cur_x = cur_x -1
        elif dir == 'R':
            if cur_x + 1 > 10:
                continue 
            if R[cur_y][cur_x] == False and L[cur_y][cur_x+1] == False:
                answer += 1
            
            R[cur_y][cur_x] = True
            cur_x = cur_x + 1

    return answer