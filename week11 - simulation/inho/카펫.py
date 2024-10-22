def solution(brown, yellow):
    sum = brown // 2 + 2
    
    for i in range(3, (sum // 2) + 1):
        j = sum - i
        if (i-2) * (j-2) == yellow:
            return [j, i]
