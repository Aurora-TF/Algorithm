def to_binary(value):
    ret = ""
    while value != 0:
        res = value % 2
        ret += str(res)
        value = value // 2
    
    return ret[::-1]

def solution(s):
    r = 0
    zero = 0
    while s != "1":
        length = 0
        for data in s:
            if data == "1":
                length += 1
            else:
                zero += 1
        
        s = to_binary(length)
        r += 1
    
    answer = [r, zero]
    return answer