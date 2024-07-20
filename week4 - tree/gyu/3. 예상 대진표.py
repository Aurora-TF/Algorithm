def calc(a):
    if a % 2 == 0:
        return a // 2
    else:
        return (a // 2) + 1

def solution(n,a,b):
    answer = 1

    a = calc(a)
    b = calc(b)
    
    if a == b:
        return answer
    
    while a != b:
        a = calc(a)
        b = calc(b)
        answer += 1
           

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer
'''
              1
      1               2
  1       2       3       4
1   2   3   4   5   6   7   8

홀수라면 = a/2 + 1
찍수라면 = a/2
같아지면 정답

'''