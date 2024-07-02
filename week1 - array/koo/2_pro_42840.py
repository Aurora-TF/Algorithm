def check_score(answers, pattern):
    length = len(pattern)
    total_problem = len(answers)
    score = 0
    
    for i in range(total_problem):
        index = i % length
        if answers[i] == pattern[index]:
            score += 1
    
    return score
        
def solution(answers):
    answer = []
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    
    score_result = []
    
    score_result.append(check_score(answers, first))
    score_result.append(check_score(answers, second))
    score_result.append(check_score(answers, third))
    
    answer.append(1)
    
    for i in range(1, 3):
        if score_result[i] > score_result[answer[0] - 1]:
            answer = [i + 1]
        elif score_result[i] == score_result[answer[0] - 1]:
            answer.append(i + 1)
    
    return answer