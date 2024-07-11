import math

def solution(progresses, speeds):
    answer = []
    queue = []
    
    for idx in range(len(progresses)):
        temp = math.ceil((100 - progresses[idx]) / speeds[idx])
        queue.append(temp)
    
    while queue:
        temp = 1
        pivot = queue.pop(0)
        
        while queue and pivot >= queue[0]:
            temp += 1
            queue.pop(0)
        
        answer.append(temp)        
    
    return answer