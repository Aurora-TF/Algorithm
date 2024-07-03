def solution(n, k, cmd):
    up = [i - 1 for i in range(n + 1)]
    down = [i + 1 for i in range(n + 1)]

    stack = []

    for c in cmd:
        if c.startswith("C"):
            stack.append(k)
            up[down[k]] = up[k]
            down[up[k]] = down[k]

            if n <= down[k]:
                k = up[k]
            else:
                k = down[k]

        elif c.startswith("Z"):
            p = stack.pop()
            up[down[p]] = p
            down[up[p]] = p
        else:
            d, x = c.split()
            if d == "U":
                for _ in range(int(x)):
                    k = up[k]
            elif d == "D":
                for _ in range(int(x)):
                    k = down[k]
    
    answer = ["O"] * n
    for p in stack:
        answer[p] = "X"

    return "".join(answer)