def solution(arr1, arr2):
    answer = []
    m = len(arr1)
    k = len(arr1[0])
    n = len(arr2[0])
    
    for i in range(m):
        answer_temp = []
        for j in range(n):
            temp = 0
            for p in range(k):
                temp += arr1[i][p] * arr2[p][j]
            answer_temp.append(temp)    
        answer.append(answer_temp)
    
    return answer