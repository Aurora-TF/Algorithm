def backtracking(k, dungeons, check, count):
    ans = count
    for i in range(len(dungeons)):
        if check[i]:
            continue
        
        if k >= dungeons[i][0]:
            check[i] = True
            ans = max(ans, backtracking(k - dungeons[i][1], dungeons, check, count + 1))
            check[i] = False

    return ans

def solution(k, dungeons):
    check = [False] * len(dungeons)
    return backtracking(k, dungeons, check, 0)