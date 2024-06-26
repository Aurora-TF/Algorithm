def grading(answers, p):
    n = len(answers)
    p_n = len(p)
    ans = 0

    for i in range(n):
        j = i % p_n
        if answers[i] == p[j]:
            ans += 1

    return ans

def solution(answers):
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    answer = []

    ans_p1 = (grading(answers, p1), 1)
    ans_p2 = (grading(answers, p2), 2)
    ans_p3 = (grading(answers, p3), 3)

    temp = [ans_p1, ans_p2, ans_p3]
    temp.sort()
    answer.append(temp[2][1])

    if temp[2][0] == temp[1][0]:
        answer.append(temp[1][1])

    if temp[2][0] == temp[0][0]:
        answer.append(temp[0][1])

    answer.sort()
    return answer