def solution(N, stages):
    answer = []
    count = len(stages)
    failure_count = [0] * (N+2)
    success_count = [count] * (N+2)
    failure_rate = [0] * (N+2)
    # [1,2,2,2,3,3,4,6]
    # [8, 7,7,7,,4,4,2,1]
    stages.sort()
    for stage in stages:
        failure_count[stage] += 1

    for i in range(1,N+1):
        success_count[i] = success_count[i-1] - failure_count[i]

    for stage in range(1,N+1):
        if success_count[stage-1] == 0:
            failure_rate[stage] = 0
            answer.append((-failure_rate[stage], stage))
            continue
        failure_rate[stage] = failure_count[stage] / success_count[stage-1]
        answer.append((-failure_rate[stage], stage))

    answer.sort()
    ret = []
    for a in answer:
        ret.append(a[1])

    return ret