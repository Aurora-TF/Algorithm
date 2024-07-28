def solution(nums):
    answer = 0
    total_length = len(nums) / 2
    
    nums = set(nums)
    set_length = len(nums)
    
    if set_length > total_length:
        answer = total_length
    else:
        answer = set_length
    
    return answer