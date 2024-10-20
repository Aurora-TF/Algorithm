def solution(topping):
    answer = 0
    
    topping_map = {}
    total_popping = len(set(topping))
    for t in topping:
        topping_map[t] = topping_map.get(t,0) + 1
    
    my_topping_map = {}
    my_topping = 0 
    for t in topping:
        if my_topping_map.get(t, 0) == 0:
            my_topping_map[t] = 1
            my_topping += 1
        topping_map[t] -= 1
        if topping_map[t] == 0:
            total_popping -= 1
        
        if total_popping == my_topping:
            answer += 1
            
    return answer