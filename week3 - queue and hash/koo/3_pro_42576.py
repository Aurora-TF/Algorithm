def solution(participant, completion):
    answer = ''
    marathon = {}
    hash_total = 0
    
    for part in participant:
        marathon[hash(part)] = part
        hash_total += hash(part)
    
    for comp in completion:
        hash_total -= hash(comp)
    
    answer = marathon[hash_total]    
        
    return answer

# def solution(participant, completion):
#     answer = ''
#     participant.sort()
#     completion.sort()
    
#     for i in range(len(completion)):
#         if completion[i] != participant[i]:
#             answer = participant[i]
#             break
#     if answer == '':
#         answer = participant[-1]
        
#     return answer