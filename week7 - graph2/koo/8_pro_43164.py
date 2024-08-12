from collections import defaultdict

def solution(tickets):
    answer = []
    stack = ["ICN"]
    cities = defaultdict(list)
    
    tickets.sort()
    
    for ticket in tickets:
        cities[ticket[0]].append(ticket[1])
    
    # city = {}
    # for t in tickets:
    #     city[t[0]] = city.get(t[0], []) + [t[1]]    
        
    while stack:
        cur = stack[-1]
                
        if cur in cities and cities[cur]:
            stack.append(cities[cur].pop(0))
        else:
            answer.append(stack.pop())
    
    return answer[::-1]