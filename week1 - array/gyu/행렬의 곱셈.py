def solution(arr1, arr2):
    answer = []

    p = len(arr1)
    n = len(arr2[0])
    m = len(arr2)

    for l in range(p):
        line = []
        for i in range(n):
            data = 0
            for k in range(m):
                data += arr1[l][k] * arr2[k][i]
            line.append(data)
        answer.append(line)

    print(answer)
    return answer
#
#[
#    [1,4],
#    [3,2],
#    [4,1]
#]
#
#[
#    [3,3],
#    [3,3]
#]
#
#[
#    [15,15],
#    [15,15],
#    [15,15]
#]
#
#
#[
#    [2,3,2],
#    [4,2,4],
#    [3,1,4]
#]