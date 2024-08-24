def solution(n):
    answer = 0
    
    def dfs(n, board, row):
        if n == row:
            return 1
        cnt = 0
        
        for col in range(n):
            board[row] = col
            
            for i in range(row):
                if board[row] == board[i]:
                    break
                    
                if abs(board[row] - board[i]) == row - i:
                    break
            else:
                cnt += dfs(n, board, row + 1)
        return cnt
    
    answer = dfs(n, [0] * n, 0)
    return answer