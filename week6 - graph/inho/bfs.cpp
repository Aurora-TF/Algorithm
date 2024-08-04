#include <string>
#include <vector>
#include <deque>
#include <iostream>
#include <set>

using namespace std;

bool isOneLetterDiff(string a, string b){
    // 그 다른게 당장은 target에 없어도 거쳐가는 path가 될수있음
    int cnt = 0;
    for(int i=0; i<a.size(); i++){
        if(a[i] != b[i]) cnt++;
    }
    return cnt == 1 ? true : false;
}

int solution(string begin, string target, vector<string> words) {
    int answer = 0;
    set<string> visit;
    deque<pair<string, int> > q;
    q.push_back({begin, 0});
    while(!q.empty()){
        auto t = q.front();
        int cnt = t.second;
        string tmp = t.first;
        
        q.pop_front();
        
        for(int i=0; i<words.size(); i++){
            string next = words[i];
            if(visit.find(next) != visit.end()) continue;
            if(!isOneLetterDiff(tmp, next)) continue;
            
            if(next == target) return cnt+1;
            // 여기서 visit처리하느냐 pop할때 하느냐
            visit.insert(next);
            q.push_back({next, cnt+1});
        }
    }
    
    
    return answer;
}

