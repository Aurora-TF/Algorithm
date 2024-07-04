def solution(n, k, cmd):
    answer = [0 for _ in range(n)]
    idx = k
    stack = []
    table = [[i - 1, i + 1, i] for i in range(n)]
    table[0][0] = 0
    table[-1][1] = n - 1
        
    for cm in cmd:
        if cm[0] == "C":
            stack.append(idx)
            answer[idx] = 1
            
            front = table[idx][0]
            rear = table[idx][1]
            
            if front == idx:
                table[rear][0] = rear
                idx = rear
            elif rear == idx:
                table[front][1] = front
                idx = front
            else:
                table[front][1] = rear
                table[rear][0] = front
                idx = rear
            
        elif cm[0] == "Z":
            tmp_idx = stack.pop()
            answer[tmp_idx] = 0           
            
            front = table[tmp_idx][0]
            rear = table[tmp_idx][1]
            
            if front == tmp_idx:
                table[rear][0] = tmp_idx
            elif rear == tmp_idx:
                table[front][1] = tmp_idx
            else:
                table[rear][0] = tmp_idx
                table[front][1] = tmp_idx    
            
        elif cm[0] == "U":
            move = int(cm.split()[1])
            for mo in range(move):
                idx = table[idx][0]                
            
        elif cm[0] == "D":
            move = int(cm.split()[1])
            for mo in range(move):
                idx = table[idx][1]
    
    temp = []
    for i in range(n):
        if answer[i] == 0:
            temp.append("O")
        else:
            temp.append("X")
    
    answer = ''.join(temp)
                
    return answer