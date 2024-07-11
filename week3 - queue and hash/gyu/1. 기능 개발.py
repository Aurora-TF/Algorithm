from collections import deque

def solution(progresses, speeds):
    q = deque()
    for i in range(len(progresses)):
        q.append(i)
    
    answer = []
    while q:
        i = q.popleft()
        if progresses[i] >= 100:
            answer[-1] += 1
            continue

        ret = 100 - progresses[i]
        offset = 0 if ret % speeds[i] == 0 else 1
        c = offset + ret // speeds[i]
        for j in range(c):
            for k in range(i,len(progresses)):
                progresses[k] += speeds[k]

        answer.append(1)
    return answer