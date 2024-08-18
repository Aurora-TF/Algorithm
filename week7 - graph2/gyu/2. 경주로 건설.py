from collections import deque

# 만약 head가 없었다면 굳이 previous_cost를 넣어주지 않아도 될 것이다. 그렇지만 head가 있기 때문에 previous_cost를 넣어야만 한다.
# 방향인 head가 있기 때문에 check로 거리를 계산할 때도, 거리가 최소인 경우에도 방향에 따라 결과가 달라질 수 있어서, 방향마다 거리의 최소를 구해야한다.
# 최소 비용이 같은 경우는 한 번 더 계산할 필요 없다.
[[0, 0, 0, 0, 0],
 [0, 1, 1, 1, 0],
 [0, 0, 1, 0, 0],
 [1, 0, 0, 0, 1],
 [1, 1, 1, 0, 0]]

N = 0
H = 1
V = 2
MAX_COST = 25 * 25 * 500 + 25*25*100      
def bfs(board):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    n = len(board)
    check = [[[MAX_COST for _ in range(3)] for _ in range(n)] for _ in range(n)]
    q = deque()
    q.append((0,0,0,N))
    check[0][0][N] = 0
    check[0][0][V] = 0
    check[0][0][H] = 0

    while q:
        y, x, previous_cost, head = q.popleft()
        for i in range(4):
            next_y = y + dy[i]
            next_x = x + dx[i]
            if next_x < 0 or next_x >= n or next_y < 0 or next_y >= n:
                continue
            
            if board[next_y][next_x]:
                continue
            
            cost = 100
            next_head = N
            if x == next_x:
                next_head = V
            elif y == next_y:
                next_head = H
                
            if head != N and next_head != head:
                cost += 500
            
            if check[next_y][next_x][next_head] <= cost + previous_cost:
                continue
            
            q.append((next_y, next_x, previous_cost + cost, next_head))
            check[next_y][next_x][next_head] = previous_cost + cost
    
    return min(check[n-1][n-1][V], check[n-1][n-1][H])

def solution(board):
    return bfs(board)