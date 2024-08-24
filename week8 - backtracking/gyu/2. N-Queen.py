def backtracking(n, y, cols, dia1, dia2, count):
    if n == y:
        return count+1
    
    ans = count
    for i in range(n):
        if cols[i] or dia1[i + y] or dia2[n - i + y]:
            continue
        cols[i] = True
        dia1[i + y] = True
        dia2[n - i + y] = True
        ans += backtracking(n, y + 1, cols, dia1, dia2,count)
        cols[i] = False
        dia1[i + y] = False
        dia2[n - i + y] = False
    
    return ans

def solution(n):
    cols = [False] * n
    dia1 = [False] * (n * 2)
    dia2 = [False] * (n * 2)
    
    return backtracking(n, 0, cols, dia1, dia2, 0)