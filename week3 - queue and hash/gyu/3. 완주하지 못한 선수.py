def solution(participant, completion):
    participant.sort()
    completion.sort()
    answer = ''

    is_find = False
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            is_find = True
            break
    
    if not is_find:
        answer = participant[-1]
        
    return answer