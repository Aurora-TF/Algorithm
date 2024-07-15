def solution(genres, plays):
    answer = []
    counts = {}
    counts_on_genres = {}

    for i in range(len(genres)):
        if not genres[i] in counts:
            counts[genres[i]] = 0
            counts_on_genres[genres[i]] = []
        counts[genres[i]] += plays[i]
        counts_on_genres[genres[i]].append((-plays[i], i))
    
    temp_counts = []
    for key in counts:
        counts_on_genres[key].sort()
        temp_counts.append((-counts[key], key))
    
    temp_counts.sort()

    for _, key in temp_counts:
        count = 0
        for _, i in counts_on_genres[key]:
            if count == 2:
                break
            answer.append(i)
            count += 1
    
    return answer