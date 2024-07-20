from collections import deque

def bfs(maps, sx, sy, ex, ey):
    n = len(maps)
    m = len(maps[0])

    check = []
    for i in range(n):
        check.append([])
        for j in range(m):
            check[i].append(False)

    q = deque()

    dx = [-1,0,1, 0]
    dy = [ 0,1,0,-1]

    q.append((sx,sy,0))
    check[sy][sx] = True
    while q:
        cx, cy, c = q.popleft()
        if cy == ey and cx == ex:
            return c
        
        for i in range(4):
            next_x = cx + dx[i]
            next_y = cy + dy[i]

            if 0 > next_x or next_x >= m or 0 > next_y or next_y >= n:
                continue

            if maps[next_y][next_x] == 'X':
                continue

            if check[next_y][next_x]:
                continue

            q.append((next_x, next_y, c + 1))
            check[next_y][next_x] = True

    return -1

def solution(maps):
    n = len(maps)
    m = len(maps[0])

    sx = 0
    sy = 0
    ex = 0
    ey = 0
    lx = 0
    ly = 0
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                sx = j
                sy = i
            elif maps[i][j] == 'E':
                ex = j
                ey = i
            elif maps[i][j] == 'L':
                lx = j
                ly = i
    
    dist1 = bfs(maps, sx, sy, lx, ly)
    if dist1 == -1:
        return -1
    
    dist2 = bfs(maps, lx, ly, ex, ey)
    if dist2 == -1:
        return -1
    
    return dist1 + dist2

print(solution(["LOOOOXX",
                "XXXXOXX",
                "OXOOOXX",
                "OXXXOOO",
                "EOXSEXO"]))