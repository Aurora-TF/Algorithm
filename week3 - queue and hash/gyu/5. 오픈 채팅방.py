from collections import deque

def solution(record):
    answer = []
    user_to_name = {}
    q = deque()

    for r in record:
        split_command = r.split()
        if split_command[0] == "Enter":
            q.append((split_command[0], split_command[1]))
            user_to_name[split_command[1]] = split_command[2]
        elif split_command[0] == "Leave":
            q.append((split_command[0], split_command[1]))
        else: # change
            user_to_name[split_command[1]] = split_command[2]
    
    while q:
        command, userId = q.popleft()
        name = user_to_name[userId]
        if command == "Enter":
            answer.append(f"{name}님이 들어왔습니다.")
        elif command == "Leave":
            answer.append(f"{name}님이 나갔습니다.")
    
    return answer