def solution(brown, yellow):
    answer = []
    total = brown + yellow
    
    for i in range(3, total // 2):
        if not total % i:
            row = total // i - 2
            col = i - 2
            if row * col == yellow:
                answer = [row + 2, col + 2]
                break
    
    return answer