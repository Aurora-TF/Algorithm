def solution(genres, plays):
    answer = []
    table = {}
    playlist = {}
    
    for i in range(len(genres)):
        if genres[i] in table:
            table[genres[i]] += plays[i]
        else:
            table[genres[i]] = plays[i]
            
        if genres[i] in playlist:
            playlist[genres[i]].append([i, plays[i]])
        else:
            playlist[genres[i]] = [[i, plays[i]]]
    
    table = sorted(table.items(), key = lambda x: -x[1])
        
    for i in range(len(table)):
        temp = sorted(playlist[table[i][0]], key = lambda x: (-x[1], x[0]))
        
        if len(temp) == 1:
            answer.append(temp[0][0])
        else:
            answer.append(temp[0][0])
            answer.append(temp[1][0])
            
    return answer