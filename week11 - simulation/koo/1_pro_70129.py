def solution(s):
    answer = []
    total_count = 0
    zero_count = 0
    
    while True:
        total_count += 1
        one_count = 0
        for i in s:
            if i == "0":
                zero_count += 1
            else:
                one_count += 1

        s = str(format(one_count, "b"))

        if s == "1":
            break
    
    answer = [total_count, zero_count]
    
    return answer