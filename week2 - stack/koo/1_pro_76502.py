def solution(s):
    answer = 0
    s = list(s)
    
    for _ in range(len(s)):
        stack = []
        for i in range(len(s)):
            if len(stack) != 0:
                if stack[-1] == '(' and s[i] == ')':
                    stack.pop()
                elif stack[-1] == '[' and s[i] == ']':
                    stack.pop()
                elif stack[-1] == '{' and s[i] == '}':
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
                
        if len(stack) == 0:
            answer += 1
        
        s.append(s.pop(0))    
    
    return answer

# 누군가 풀어둔 광기의 풀이 붙여봅니다.
# def solution(s):
#     tmp_s = s
#     answer = 0
#     if len(s) % 2 == 1: return answer
#     for i in range(len(s)):
#         t = tmp_s.replace("()", "").replace("{}", "").replace("[]", "")
#         t = t.replace("{}", "").replace("[]", "").replace("()", "")
#         t = t.replace("[]", "").replace("()", "").replace("{}", "")
#         t = t.replace("()", "").replace("{}", "").replace("[]", "")
#         t = t.replace("{}", "").replace("[]", "").replace("()", "")
#         t = t.replace("[]", "").replace("()", "").replace("{}", "")
#         t = t.replace("()", "").replace("{}", "").replace("[]", "")
#         t = t.replace("{}", "").replace("[]", "").replace("()", "")
#         t = t.replace("[]", "").replace("()", "").replace("{}", "")
#         t = t.replace("()", "").replace("{}", "").replace("[]", "")
#         t = t.replace("{}", "").replace("[]", "").replace("()", "")
#         t = t.replace("[]", "").replace("()", "").replace("{}", "")
#         t = t.replace("()", "").replace("{}", "").replace("[]", "")
#         t = t.replace("{}", "").replace("[]", "").replace("()", "")
#         t = t.replace("[]", "").replace("()", "").replace("{}", "")
#         t = t.replace("()", "").replace("{}", "").replace("[]", "")
#         t = t.replace("{}", "").replace("[]", "").replace("()", "")
#         t = t.replace("[]", "").replace("()", "").replace("{}", "")
#         t = t.replace("()", "").replace("{}", "").replace("[]", "")
#         t = t.replace("{}", "").replace("[]", "").replace("()", "")
#         t = t.replace("[]", "").replace("()", "").replace("{}", "")
#         t = t.replace("()", "").replace("{}", "").replace("[]", "")
#         t = t.replace("{}", "").replace("[]", "").replace("()", "")
#         t = t.replace("[]", "").replace("()", "").replace("{}", "")
#         t = t.replace("{}", "").replace("[]", "").replace("()", "")
#         t = t.replace("[]", "").replace("()", "").replace("{}", "")
#         t = t.replace("()", "").replace("{}", "").replace("[]", "")
#         t = t.replace("{}", "").replace("[]", "").replace("()", "")
#         t = t.replace("[]", "").replace("()", "").replace("{}", "")
#         t = t.replace("()", "").replace("{}", "").replace("[]", "")
#         t = t.replace("{}", "").replace("[]", "").replace("()", "")
#         t = t.replace("[]", "").replace("()", "").replace("{}", "")
#         t = t.replace("()", "").replace("{}", "").replace("[]", "")
#         t = t.replace("{}", "").replace("[]", "").replace("()", "")
#         t = t.replace("[]", "").replace("()", "").replace("{}", "")
#         t = t.replace("()", "").replace("{}", "").replace("[]", "")
#         t = t.replace("{}", "").replace("[]", "").replace("()", "")
#         t = t.replace("[]", "").replace("()", "").replace("{}", "")
#         t = t.replace("()", "").replace("{}", "").replace("[]", "")
#         t = t.replace("{}", "").replace("[]", "").replace("()", "")
#         t = t.replace("[]", "").replace("()", "").replace("{}", "")
#         t = t.replace("()", "").replace("{}", "").replace("[]", "")
#         t = t.replace("{}", "").replace("[]", "").replace("()", "")
#         t = t.replace("[]", "").replace("()", "").replace("{}", "")
#         t = t.replace("()", "").replace("{}", "").replace("[]", "")
#         t = t.replace("{}", "").replace("[]", "").replace("()", "")
#         t = t.replace("[]", "").replace("()", "").replace("{}", "")
#         t = t.replace("()", "").replace("{}", "").replace("[]", "")
#         t = t.replace("{}", "").replace("[]", "").replace("()", "")
#         t = t.replace("[]", "").replace("()", "").replace("{}", "")
#         t = t.replace("()", "").replace("{}", "").replace("[]", "")
#         t = t.replace("{}", "").replace("[]", "").replace("()", "")
#         t = t.replace("[]", "").replace("()", "").replace("{}", "")
#         t = t.replace("()", "").replace("{}", "").replace("[]", "")
#         t = t.replace("{}", "").replace("[]", "").replace("()", "")
#         t = t.replace("[]", "").replace("()", "").replace("{}", "")
#         t = t.replace("()", "").replace("{}", "").replace("[]", "")
#         t = t.replace("{}", "").replace("[]", "").replace("()", "")
#         t = t.replace("[]", "").replace("()", "").replace("{}", "")
#         t = t.replace("()", "").replace("{}", "").replace("[]", "")
#         t = t.replace("{}", "").replace("[]", "").replace("()", "")
#         t = t.replace("[]", "").replace("()", "").replace("{}", "")
#         t = t.replace("()", "").replace("{}", "").replace("[]", "")
#         t = t.replace("{}", "").replace("[]", "").replace("()", "")
#         t = t.replace("[]", "").replace("()", "").replace("{}", "")
#         t = t.replace("()", "").replace("{}", "").replace("[]", "")
#         t = t.replace("{}", "").replace("[]", "").replace("()", "")
#         t = t.replace("[]", "").replace("()", "").replace("{}", "")
#         t = t.replace("()", "").replace("{}", "").replace("[]", "")
#         t = t.replace("{}", "").replace("[]", "").replace("()", "")
#         t = t.replace("[]", "").replace("()", "").replace("{}", "")
#         t = t.replace("()", "").replace("{}", "").replace("[]", "")
#         t = t.replace("{}", "").replace("[]", "").replace("()", "")
#         t = t.replace("[]", "").replace("()", "").replace("{}", "")
#         t = t.replace("()", "").replace("{}", "").replace("[]", "")
#         t = t.replace("{}", "").replace("[]", "").replace("()", "")
#         t = t.replace("[]", "").replace("()", "").replace("{}", "")
#         t = t.replace("()", "").replace("{}", "").replace("[]", "")
#         t = t.replace("{}", "").replace("[]", "").replace("()", "")
#         t = t.replace("[]", "").replace("()", "").replace("{}", "")
#         t = t.replace("()", "").replace("{}", "").replace("[]", "")
#         t = t.replace("{}", "").replace("[]", "").replace("()", "")
#         t = t.replace("[]", "").replace("()", "").replace("{}", "")
#         t = t.replace("()", "").replace("{}", "").replace("[]", "")
#         if t == "":
#             answer += 1
#         tmp_s = tmp_s[1:] + tmp_s[0]

#     return answer