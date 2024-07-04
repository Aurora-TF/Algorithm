def solution(s):
    answer = 0
    stack = []
    for t in s:
        if not stack:
            stack.append(t)
        elif t == stack[-1]:
            stack.pop()
        else:
            stack.append(t)
    
    if not stack:
        answer += 1

    return answer