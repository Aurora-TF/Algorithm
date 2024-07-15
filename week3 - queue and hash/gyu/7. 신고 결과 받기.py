def solution(id_list, report, k):
    answer = []
    reported_table = {}
    report_from = {}
    for c in report:
        f, t = tuple(c.split())
        if t not in reported_table:
            reported_table[t] = set()
            
        if f not in report_from:    
            report_from[f] = set()

        reported_table[t].add(f)
        report_from[f].add(t)
    
    for name in id_list:
        answer.append(0)
        if name in report_from:
            for target in report_from[name]:
                if len(reported_table[target]) >= k:
                    answer[-1] += 1
    
    return answer