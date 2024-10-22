def solution(s):
    transCnt, zeroCnt = 0 , 0
    while s != '1':
        transCnt += 1
        zeroCnt += s.count('0')
        s = bin(s.count('1'))[2:]
    answer = [transCnt, zeroCnt]
    return answer