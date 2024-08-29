from itertools import permutations

def solution(n, weak, dist):
    # Step 1: 두 배로 확장된 weak 리스트 생성 -> 원형을 직선으로 표시하기 위함
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
    
    answer = len(dist) + 1
    for start in range(length):
        for friends in permutations(dist):
            count = 1
            position = weak[start] + friends[count - 1]
            
            for index in range(start, start + length):
                if position < weak[index]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[index] + friends[count - 1]
            answer = min(answer, count)
    
    if answer > len(dist):
        return -1
    return answer