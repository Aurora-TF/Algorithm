import sys
sys.setrecursionlimit(10**6)
def backtracking(numbers, index,target, total, ans):
    if index == len(numbers):
        if target == total:
            return 1
            
        return 0
    
    ans = (backtracking(numbers, index + 1, target, total + numbers[index], ans) + backtracking(numbers, index + 1, target, total - numbers[index], ans))
    return ans

def solution(numbers, target):
    return backtracking(numbers, 0, target, 0, 0)