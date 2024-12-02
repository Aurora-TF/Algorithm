data = [1, 4, 2, 3, 1, 5, 7, 3] 
lis = []

def LIS(n, data, lis):
    if n == 0:
        return 1
    
    ret = 0
    for k in range(n):
        if data[k] < data[n] and ret < lis[k]:
            ret = lis[k]
    
    return ret + 1

for i in range(len(data)):
    lis.append(0)

max_val = 0
for i in range(len(data)):
    lis[i] = LIS(i, data, lis)
    if lis[i] > max_val:
        max_val = lis[i]
        
print("LIS:", lis) # LIS: [1, 2, 2, 3, 1, 4, 5, 3]
print("LEN:", max_val) # LEN: 5