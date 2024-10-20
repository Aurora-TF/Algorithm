# w,h 가 있다면 w-2 * h -2가 노란 타일의 갯수
# brwon + yello = total에서 w를 하나씩 늘려나가 h를 구하고, yello로 갯수와 맞으면 정답

def solution(brown, yellow):
    total = brown + yellow
    answer = []
    
    for w in range(3, total):
        if total % w != 0:
            continue
        
        h = total // w
        if (w-2)*(h-2) == yellow:
            answer.append(w)
            answer.append(h)
            break
    
    answer.sort(reverse=True)
    return answer