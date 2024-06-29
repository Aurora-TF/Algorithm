#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

bool cmp(const pair<int, double> a, const pair<int, double> b) {
    if (a.second == b.second) return a.first < b.first;
    return a.second > b.second;
}

// 2의 실패율은 (2 갯수 / 2이상인 갯수);
// n의 실패율은 (n 갯수 / n이상인 갯수);
// n갯수가 0 이면 실패율 0;
// n갯수가 있는데 n 이상인 갯수가 없을순 없음.;
// 대신 n갯수가 0 인경우는 예외처리필요;

vector<int> solution(int N, vector<int> stages){
    vector<int> answer;
    
    vector<int> failUserCnt(N+2);
    vector<int> reachUserCnt(N+2);
    vector<pair<int, double> > stageFailure;
    
    for(int i=0; i<stages.size(); i++)
        failUserCnt[stages[i]]++;
    
    int acc = 0;
    for(int i=1; i < N+1; i++){
        // i단계 통과 유저 = 전체유저 - 1 ~ i-1 단계에 있는 유저
        reachUserCnt[i] = stages.size() - acc;
        acc += failUserCnt[i];
        stageFailure.push_back({i, reachUserCnt[i] == 0 ? 0 :failUserCnt[i]/(double)reachUserCnt[i]});
    }
    
    sort(stageFailure.begin(), stageFailure.end(), cmp);
    
    for(int i=0; i<N; i++){
        answer.push_back(stageFailure[i].first);
    }
    
    return answer;
}

