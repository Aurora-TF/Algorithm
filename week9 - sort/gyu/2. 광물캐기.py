ans = float('inf')

def dfs(picks, minerals, index, count):
    global ans
    mapper = {
        0: [1, 1, 1],
        1: [5, 1, 1],
        2: [25, 5, 1]
    }
    
    if count >= ans:
        return
    
    if index >= len(minerals) or sum(picks) == 0:
        ans = min(ans, count)
        return
    
    for i in range(3):
        if picks[i] <= 0:
            continue
        
        picks[i] -= 1
        offset = 0 
        for j in range(5):
            if index + j >= len(minerals):
                break
            if minerals[index+j] == 'diamond':
                offset += mapper[i][0]
            elif minerals[index+j] == 'iron':
                offset += mapper[i][1]
            else:
                offset += mapper[i][2]
        
        dfs(picks, minerals, index + 5, count + offset)
        picks[i] += 1

def solution(picks, minerals):
    global ans
    dfs(picks, minerals, 0, 0)
    return ans