#include <string>
#include <vector>
#include <memory.h>
#include <iostream>

// 내 앞에 몇명 뒤에 몇명이 확실하면 되는거같은데
// 내 위방향 탐색 + 내 밑방향 탐색 해서 전체노드를 들리면 가능?

using namespace std;

vector<vector<int>> adjU;
vector<vector<int>> adjD;
bool visit[101];
void dfsUp(int node){
    visit[node] = true;
    for(auto i : adjU[node]){
        if(!visit[i])
            dfsUp(i);
    }
}

void dfsDown(int node){
    visit[node] = true;
    for(auto i : adjD[node]){
        if(!visit[i])
            dfsDown(i);
    }
}

bool checkVisitedAll(int n){
    for(int i=1; i<=n; i++){
        if(!visit[i]) return false;
    }
    return true;
}

int solution(int n, vector<vector<int>> results) {
    int cnt = 0;
    adjU = vector<vector<int>>(101, vector<int>());
    adjD = vector<vector<int>>(101, vector<int>());
    
    for(auto i : results){
        adjD[i[0]].push_back(i[1]);
        adjU[i[1]].push_back(i[0]);
    }
    
    for(int i=1; i<=n; i++){
        memset(visit, false, sizeof(visit));
        dfsUp(i);
        dfsDown(i);
        if (checkVisitedAll(n)) cnt++;
    }
    
    return cnt;
}