def solution(numbers):
    answer = ''
    
    numbers = list(map(str, numbers))   
    numbers.sort(key = lambda x : x * 3, reverse=True) 
    
    for i in numbers:     
        answer += i
    
    return str(int(answer))

# https://esoongan.tistory.com/103

# from itertools import permutations

# def solution(numbers):
#     answer = ''
#     possible = list(permutations(numbers, len(numbers)))
#     max_num = 0
    
#     for pos in possible:
#         num = "".join(map(str, pos))
#         max_num = max(max_num, int(num))
#     answer = str(max_num)
    
#     return answer