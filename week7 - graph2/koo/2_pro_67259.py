from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(board, direct):
    n = len(board)
    price = [[int(1e9)] * n for _ in range(n)]
    price[0][0] = 0
    
    que = deque()
    que.extend([(0, 0, 0, direct)])
    
    while que:
        x, y, c, z = que.popleft()
        
        if x == n - 1 and y == n - 1:
            continue
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = i
            nc = 0
            
            if 0 <= nx <= (n - 1) and 0 <= ny <= (n - 1) and board[nx][ny] == 0:
                if nz == z:
                    nc = c + 100
                else:
                    nc = c + 600
                    
                if nc <= price[nx][ny]:
                    price[nx][ny] = nc
                    que.append((nx, ny, nc, i))

    return price[-1][-1]

def solution(board):
    n = len(board)
    answer = min(bfs(board, 0), bfs(board, 2))
    return answer

# 25번 tc 실패
# from collections import deque

# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]

# def bfs(board):
#     n = len(board)
#     price = [[int(1e9)] * n for _ in range(n)]
#     price[0][0] = 0
#     price[0][1] = 100
#     price[1][0] = 100
    
#     que = deque()
#     que.extend([(0, 0, 0, 0), (0, 0, 0, 2)])
    
#     while que:
#         x, y, c, z = que.popleft()
        
#         if x == n - 1 and y == n - 1:
#             continue
        
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             nz = i
#             nc = 0
            
#             if 0 <= nx <= (n - 1) and 0 <= ny <= (n - 1) and board[nx][ny] == 0:
#                 if nz == z:
#                     nc = c + 100
#                 else:
#                     nc = c + 600
                    
#                 if nc <= price[nx][ny]:
#                     price[nx][ny] = nc
#                     que.append((nx, ny, nc, i))

#     return price[-1][-1]

# def solution(board):
#     n = len(board)
#     answer = bfs(board)
#     return answer