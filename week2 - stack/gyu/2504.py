import sys

inputs = sys.stdin.readline
target = inputs().strip()

stack = []

for c in target:
    if stack and stack[-1] == '(' and c == ')':
        stack.pop()
    elif stack and stack[-1] == '[' and c == ']':
        stack.pop()
    else:
        stack.append(c)

if stack:
    print(0)
else:
    ans = 0
    stack = []
    for c in target:
        if stack and stack[-1] == '(' and c == ')':
            stack.pop()
            stack.append(2)
        elif stack and stack[-1] == '[' and c == ']':
            stack.pop()
            stack.append(3)
        elif stack and c == ')':
            s = 0
            while stack[-1] != '(':
                v = stack.pop()
                s += v
            stack.pop()
            s *= 2
            stack.append(s)
        elif stack and c == ']':
            s = 0
            while stack[-1] != '[':
                v = stack.pop()
                s += v
            stack.pop()
            s *= 3
            stack.append(s)
        else:
            stack.append(c)
    for v in stack:
        ans += v

    print(ans)
        