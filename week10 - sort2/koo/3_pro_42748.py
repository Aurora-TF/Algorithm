def solution(array, commands):
    answer = []
    
    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]
        temp = array[i - 1:j]
        temp.sort()
        answer.append(temp[k - 1])
    return answer