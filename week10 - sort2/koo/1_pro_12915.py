def solution(strings, n):
    answer = []
    
    strings.sort()
    strings.sort(key = lambda x : x[n])
    answer = strings
    return answer