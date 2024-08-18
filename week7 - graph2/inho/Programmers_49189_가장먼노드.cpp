#include <string>
#include <vector>
#include <deque>
#include <iostream>
#include <memory.h>

bool visit[20001];
using namespace std;

int solution(int n, vector<vector<int>> edge) {
    deque<pair<int, int>> q;
    vector<vector<int>> adj(20001, vector<int>());
    
    for(auto tmp : edge){
        adj[tmp[0]].push_back(tmp[1]);
        adj[tmp[1]].push_back(tmp[0]);
    }
    
    memset(visit, false, sizeof(visit));
    q.push_back({1, 0});
    visit[1] = true;
    int maxValue = 0;
    int maxCnt = 0;
    while(!q.empty()){
        auto tmp = q.front();
        int cnt = tmp.second;
        q.pop_front();
        
        if(cnt > maxValue){
            maxValue = cnt;
            maxCnt = 1;
        }else if(cnt == maxValue){
            maxCnt++;
        }
        
        for(int i : adj[tmp.first]){
            if(visit[i]) continue;
            
            visit[i] = true;
            q.push_back({i, cnt+1});
        }
    }
    
    return maxCnt;
}