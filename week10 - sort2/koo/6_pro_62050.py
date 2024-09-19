from collections import deque
import heapq
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def solution(land, height):
    answer = 0
    n = len(land)
    visit = [[0] * n for _ in range(n)]
    heap = [[0, 0, 0]] # cost, x, y
    
    while heap:
        c, x, y = heapq.heappop(heap)
        if visit[x][y]:
            continue
        visit[x][y] = True
        answer += c
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny]:
                if abs(land[x][y] - land[nx][ny]) > height:
                    heapq.heappush(heap, [abs(land[x][y] - land[nx][ny]), nx, ny])
                else:
                    heapq.heappush(heap, [0, nx, ny])
                    
    return answer