

def solution(nums):
    kind = set()
    candidate = len(nums) // 2
    
    for target in nums:
        kind.add(target)
    
    answer = len(kind) if len(kind) < candidate else candidate
    return answer