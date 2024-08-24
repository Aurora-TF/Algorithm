import copy
# import sys
# sys.setrecursionlimit(10**9)
brian_array = [0] * 11
brian_max = 0

def backtracking(n, k,me,info):
    if n == 0:
        apeach = 0
        brian = 0
        for i in range(len(info)):
            if me[i] > info[i]:
                brian += 10 - i
            elif info[i] != 0:
                apeach += 10 - i
        
        global brian_array
        global brian_max
        if brian > apeach:
            if brian - apeach > brian_max:
                brian_max = brian - apeach
                brian_array = copy.deepcopy(me)
            elif brian - apeach == brian_max:
                for i in range(len(info)):
                    if me[10-i] == brian_array[10-i]:
                        continue
                    
                    if me[10-i] > brian_array[10-i]:
                        brian_array = copy.deepcopy(me)
                    break
        return

    if k >= len(info):
        return
                
    for i in range(0,n+1):
        me[k] += i
        backtracking(n-i, k+1, me, info)
        me[k] -= i

def solution(n, info):    
    backtracking(n, 0,[0] * len(info), info)
    global brian_array
    global brian_max
    if brian_max == 0:
        return [-1]
    return brian_array