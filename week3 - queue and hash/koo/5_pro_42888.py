def solution(record):
    answer = []
    queue = []
    data = {}
    
    for rec in record:
        temp = rec.split()
        
        if temp[0] == "Enter":
            data[temp[1]] = temp[2]
            queue.append([temp[1], 1])
        elif temp[0] == "Leave":
            queue.append([temp[1], 0])
        elif temp[0] == "Change":
            data[temp[1]] = temp[2]
    
    for que in queue:
        if que[1] == 1:
            answer.append(data[que[0]] + "님이 들어왔습니다.")
        elif que[1] == 0:
            answer.append(data[que[0]] + "님이 나갔습니다.")
    
    return answer