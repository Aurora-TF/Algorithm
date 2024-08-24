def solution(n, info):
    global answer, diff, ryan
    answer = []
    ryan = [0] * 11
    diff = 0
    
    def dfs(m, idx):
        global answer, diff, ryan
        
        if m == n:
            r_score = 0
            a_score = 0
            
            for i in range(11):
                if ryan[i] > info[i]:
                    r_score += 10 - i
                elif info[i] != 0 and ryan[i] <= info[i]:
                    a_score += 10 - i
                    
            if r_score > a_score:
                if diff < r_score - a_score:
                    diff = r_score - a_score
                    answer = ryan[:]
                elif diff == r_score - a_score:
                    for i in range(10, -1, -1):
                        if ryan[i] < answer[i]:
                            break
                        if ryan[i] > answer[i]:
                            answer = ryan[:]
                            break
            return
        
        for i in range(idx, 11):
            ryan[i] += 1
            dfs(m + 1, i)
            ryan[i] -= 1
        
    dfs(0, 0)
    
    return answer if answer else [-1]