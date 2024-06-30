def solution(N, stages):
    answer = []
    answer_with_index = []
    user_num = len(stages)
    failure_stage = [0 for i in range(N + 1)]
    failure_cnt = 0
    
    for i in range(user_num):
        failure_stage[stages[i] - 1] += 1

    for i in range(N):
        temp = user_num - failure_cnt
        
        if temp == 0:
            for i in range(i, N):
                answer_with_index.append([0, i + 1])
            break    
                
        rate = failure_stage[i] / temp        
        answer_with_index.append([rate, i + 1])
        
        failure_cnt += failure_stage[i]
    
    answer_with_index = sorted(answer_with_index, key = lambda x: (-x[0], x[1]))
    
    for i in range(len(answer_with_index)):
        answer.append(answer_with_index[i][1])
    
    return answer