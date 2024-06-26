def solution(numbers):
    temp = []
    n = len(numbers)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue

            temp.append(numbers[i] + numbers[j])
            
    answer = list(set(temp))
    answer.sort()
    return answer

