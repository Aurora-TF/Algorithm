def solution(picks, minerals):
    answer = 0
    total = sum(picks)
    
    possible = total * 5
    if len(minerals) > possible:
        minerals = minerals[:possible]
    
    new_minerals = [[0, 0, 0] for _ in range(len(minerals) // 5 + 1)]
    for m in range(len(minerals)):
        if minerals[m] == 'diamond':
            new_minerals[m // 5][0] += 1
        elif minerals[m] == 'iron':
            new_minerals[m // 5][1] += 1
        elif minerals[m] == 'stone':
            new_minerals[m // 5][2] += 1
            
    new_minerals.sort(key = lambda x : (x[0], x[1], x[2]), reverse = True)
    
    for i in new_minerals:
        dia, iron, stone = i
        
        for j in range(len(picks)):
            if picks[j] > 0 and j == 0:
                picks[j] -= 1
                answer += dia + iron + stone
                break
            elif picks[j] > 0 and j == 1:
                picks[j] -= 1
                answer += dia * 5 + iron + stone
                break
            elif picks[j] > 0 and j == 2:
                picks[j] -= 1
                answer += dia * 25 + iron * 5 + stone
                break        
    
    return answer