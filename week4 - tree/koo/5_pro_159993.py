import collections

def bfs(start_x, start_y, target_x, target_y, table):
    move= [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    que = collections.deque()
    que.append((start_x, start_y, 0))
    
    visit = [[0 for _ in range(len(table[0]))] for _ in range(len(table))]
    visit[start_x][start_y] = 1
    
    while que:
        x, y, cnt = que.popleft()
        if x == target_x and y == target_y:
            return cnt
        
        for mx, my in move:
            nx = x + mx
            ny = y + my
            
            if 0 <= nx < len(table) and 0 <= ny < len(table[0]) and table[nx][ny] != 'X' and visit[nx][ny] != 1:
                visit[nx][ny] = 1
                que.append((nx, ny, cnt + 1))
                
    return -1

def solution(maps):
    answer = 0
    
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == "S":
                sx, sy = i, j
            elif maps[i][j] == "L":
                lx, ly = i, j
            elif maps[i][j] == "E":
                ex, ey = i, j
    
    to_lever = bfs(sx, sy, lx, ly, maps)
    to_exit = bfs(lx, ly, ex, ey, maps)
    
    answer = to_lever + to_exit
    
    if to_lever == -1 or to_exit == -1:
        answer = -1
    
    return answer