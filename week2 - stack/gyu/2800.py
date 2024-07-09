import sys
from itertools import combinations

inputs = sys.stdin.readline
target = inputs()

stack = []
parenthesis = []
for i in range(len(target)):
    if target[i] == '(':
        stack.append(i)
    elif target[i] == ')' and stack:
        top = stack.pop()
        parenthesis.append((top, i))

ans = []
for i in range(1, len(parenthesis) + 1):
    combList = list(combinations(parenthesis, i))
    for comb in combList:
        parenthesis_check = [False] * len(target)
        for c in comb:
            start = c[0]
            last = c[1]
            parenthesis_check[start] = True
            parenthesis_check[last] = True
            
        v = ""
        for j in range(len(target)):
            if not parenthesis_check[j]:
                v += target[j]
        ans.append(v.strip())

ret = list(set(ans))
ret.sort()
for v in ret:
    print(v)