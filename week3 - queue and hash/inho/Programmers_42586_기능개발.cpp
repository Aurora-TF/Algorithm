#include <string>
#include <vector>
#include <deque>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    deque<pair<int, int>> dq;
    
    for(int i=0; i<progresses.size(); i++){
        dq.push_back({i, progresses[i]});
    }
    
    while(!dq.empty()){
        // 매번순환하면서 퍼센트씩 증가
        for(int i=0; i<dq.size(); i++){
            dq[i].second += speeds[dq[i].first];
        }
        int cnt = 0;
        while(!dq.empty()){
            if(dq.front().second >= 100){
                cnt++;
                dq.pop_front();
            }else{
                break;
            }
        }
        if (cnt > 0) answer.push_back(cnt);
    }
    
    // top부터 pop하기
    
    return answer;
}