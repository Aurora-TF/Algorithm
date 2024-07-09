import sys
inputs = sys.stdin.readline

n = int(inputs())

for _ in range(n):
    stack = []
    target = inputs().strip()
    for p in target:
        if stack and p == ')' and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(p)
    
    if stack:
        print("NO")
    else:
        print("YES")