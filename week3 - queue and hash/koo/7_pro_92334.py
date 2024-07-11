from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    report_list = defaultdict(set) 
    count_list = defaultdict(int)
    
    for rep in report:
        reporter, target = rep.split()
        if target in report_list[reporter]:
            continue
            
        report_list[reporter].add(target)
        count_list[target] += 1
        
    for i in id_list:
        cnt = 0
        for target in report_list[i]:
            if count_list[target] >= k:
                cnt += 1
        answer.append(cnt)
    
    return answer