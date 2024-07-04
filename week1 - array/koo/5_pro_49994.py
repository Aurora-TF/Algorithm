def solution(dirs):
    answer = 0
    
    UP = [[0] * 11 for _ in range(11)]
    DOWN = [[0] * 11 for _ in range(11)]
    LEFT = [[0] * 11 for _ in range(11)]
    RIGHT = [[0] * 11 for _ in range(11)]
    
    pos_x = 5
    pos_y = 5
    
    for dir in dirs:
        if dir == "U":
            if pos_y == 0:
                continue
            if UP[pos_y][pos_x] == 0 and DOWN[pos_y - 1][pos_x] == 0:
                answer += 1
                
            UP[pos_y][pos_x] = 1
            pos_y -= 1        
        elif dir == "D":
            if pos_y == 10:
                continue
            if DOWN[pos_y][pos_x] == 0 and UP[pos_y + 1][pos_x] == 0:
                answer += 1
            
            DOWN[pos_y][pos_x] = 1
            pos_y += 1        
        elif dir == "L":
            if pos_x == 0:
                continue
            if LEFT[pos_y][pos_x] == 0 and RIGHT[pos_y][pos_x - 1] == 0:
                answer += 1
            
            LEFT[pos_y][pos_x] = 1
            pos_x -= 1
        elif dir == "R":
            if pos_x == 10:
                continue
            if RIGHT[pos_y][pos_x] == 0 and LEFT[pos_y][pos_x + 1] == 0:
                answer += 1
            
            RIGHT[pos_y][pos_x] = 1
            pos_x += 1
    
    return answer