def solution(n, words):
    answer = []
    history = []
    
    for i in range(len(words)):
        if not history:
            history.append(words[i])
            continue
        
        if words[i] in history:            
            answer.append(i % n + 1)
            answer.append(i // n + 1)
            break
        
        if history[-1][-1] != words[i][0]:
            answer.append(i % n + 1)
            answer.append(i // n + 1)
            break
        
        history.append(words[i])
    
    if answer == []:
        answer = [0, 0]
        
    return answer