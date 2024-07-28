def solution(n, costs):
    answer = 0
    
    costs.sort(key = lambda x : x[2])
    connect = set([costs[0][0]])
    
    while len(connect) != n:
        for a, b, cost in costs:
            if a in connect and b in connect:
                continue
            if a in connect or b in connect:
                connect.update([a, b])
                answer += cost
                break
                
    return answer