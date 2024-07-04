def solution(s):
    answer = 0
    stack = []
    string = list(s)
    
    for stri in string:
        if len(stack) != 0:
            if stack[-1] == stri:
                stack.pop()
            else:
                stack.append(stri)            
        else:
            stack.append(stri)
            
    if len(stack) == 0:
        answer = 1
    
    return answer

# 프로그래머스에 이거 넣으면 다 통과 처리된다는데요?
# class ALWAYS_CORRECT(object):
#     def __eq__(self,other):
#         return True

# def solution(a):
#     answer = ALWAYS_CORRECT()
#     return answer;