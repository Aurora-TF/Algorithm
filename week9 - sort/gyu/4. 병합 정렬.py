import sys
inputs = sys.stdin.readline
print = sys.stdout.write

n = int(inputs())
nums = []
temp = [0] * n

for i in range(n):
    v = int(inputs())
    nums.append(v)

def merge(s, e):
    if s == e:
        return

    mid = (s + e) // 2
    i = s
    j = mid + 1
    c = s

    while i <= mid and j <= e:
        if nums[i] < nums[j]:
            temp[c] = nums[i]
            c += 1
            i += 1
        else:
            temp[c] = nums[j]
            c += 1
            j += 1

    while i <= mid:
        temp[c] = nums[i]
        c += 1
        i += 1
    while j <= e:
        temp[c] = nums[j]
        c += 1
        j += 1

    for k in range(s, e+1):
        nums[k] = temp[k]

def divide(s, e):
    if s < e:
        mid = (s + e) // 2
        divide(s, mid)
        divide(mid + 1, e)
        merge(s,e)

divide(0, n-1)

for i in range(n):
    print(str(nums[i]) + '\n')