from itertools import combinations

def solution(orders, course):
    answer = []
    for c in course:
        data = {}
        for order in orders:
            if len(order) >= c:
                comb_list = combinations(order, c)
                for comb in comb_list:
                    sorted_comb = sorted(comb)
                    key = "".join(sorted_comb)
                    if key not in data:
                        data[key] = 0
                    data[key] += 1
        
        max_val = 0
        max_list = []
        for key in data:
            if data[key] >= max_val:
                if data[key] > max_val:
                    max_list.clear()
                max_val = data[key]
                max_list.append(key)

        for key in max_list:
            if max_val >= 2:
                answer.append(key)

    answer.sort()
    return answer