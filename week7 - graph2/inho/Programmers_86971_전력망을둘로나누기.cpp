#include <string>
#include <vector>
#include <iostream>
#include <memory.h>
#include <math.h>

using namespace std;

vector<vector<int>> adj;
int visit[101];
int dfs(int a){
    if(visit[a]) return 0;
    visit[a] = true;
    int mine = 1;
    
    for(int tmp : adj[a]){
        mine += dfs(tmp);
    }
    return mine;
}

int solution(int n, vector<vector<int>> wires) {
    
    adj = vector<vector<int>>(n+1, vector<int>());
    for(auto list : wires){
        adj[list[0]].push_back(list[1]);
        adj[list[1]].push_back(list[0]);
    }
    
    int min = 1000;
    for(auto list : wires){
        memset(visit, false, sizeof(visit));
        visit[list[1]] = true;
        int firstCnt = dfs(list[0]);
        
        memset(visit, false, sizeof(visit));
        visit[list[0]] = true;
        int secondCnt = dfs(list[1]);
        
        min = min < abs(firstCnt-secondCnt) ? min : abs(firstCnt-secondCnt);
    }
    return min;
}