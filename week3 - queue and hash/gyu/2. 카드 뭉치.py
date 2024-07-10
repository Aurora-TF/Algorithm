
def solution(cards1, cards2, goal):
    answer = ''
    i = 0
    j = 0
    answer = "Yes"
    for word in goal:
        if i < len(cards1) and cards1[i] == word:
            i += 1
        elif j < len(cards2) and cards2[j] == word:
            j += 1
        else:
            answer = "No"
            break
    
    return answer