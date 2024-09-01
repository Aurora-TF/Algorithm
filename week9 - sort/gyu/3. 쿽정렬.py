n = 5
data = [5,3,4,2,6]
def swap(i, j):
    global data
    temp = data[i]
    data[i] = data[j]
    data[j] = temp

def partition(left, right):
    global data

    p = (left + right) // 2 # shuffle 효과를 통한 최악의 경우 n^2를 벗어난다.
    swap(left, p)
    p = left
    low = left + 1
    high = right

    while low <= high:
        while low <= high and data[low] < data[p]:
            low += 1
        while low <= high and data[high] > data[p]:
            high -= 1
        if low <= high:
            swap(low, high)
            low += 1
            high -= 1
        
    swap(p, high)
    return high

def quick_sort(left, right):
    if left < right:
        p = partition(left, right)
        quick_sort(left, p-1)
        quick_sort(p+1, right)

quick_sort(0, n-1)
print(data)