def solution(k, dungeons):
    global visit, answer
    visit = [0] * len(dungeons)
    answer = -1
    
    def dfs(stamina):
        global visit, answer
        for i in range(len(dungeons)):
            if visit[i] == 0:
                least = dungeons[i][0]
                use = dungeons[i][1]
                if stamina >= least:
                    visit[i] = 1
                    dfs(stamina - use)
                    visit[i] = 0
        answer = max(visit.count(1), answer)
        
    dfs(k)    
    
    return answer