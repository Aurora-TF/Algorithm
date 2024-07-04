def is_correct(target):
    stack = []
    for unit in target:
        i = len(stack)
        if i == 0:
            stack.append(unit)
            continue
        elif stack[i-1] == '[' and unit == ']':
            stack.pop()
        elif stack[i-1] == '{' and unit == '}':
            stack.pop()
        elif stack[i-1] == '(' and unit == ')':
            stack.pop()
        else:
            stack.append(unit)

    if len(stack) == 0:
        return 1

    return 0

def solution(s):
    answer = 0
    length = len(s)
    for i in range(length):
        target = s[i:]
        for j in range(i):
            target += s[j]
        
        answer += is_correct(target)

    return answer