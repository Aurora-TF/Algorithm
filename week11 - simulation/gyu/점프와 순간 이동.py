def solution(n):
    ans = 0
    
    while n != 0:
        res = n % 2
        n = n // 2
        if res != 0:
            ans += 1

    return ans