#include <iostream>
#include <vector>
#include <queue>
using namespace std;

#define inf 1000000

int solution(int N, vector<vector<int> > road, int K) {
    int answer = 0;
    vector<int> dist(N, inf);
    vector<pair<int, int>> graph[N];
    
    priority_queue<pair<int, int>> pq;

    for(auto r : road){
        graph[r[0]-1].push_back({r[1]-1, r[2]});
        graph[r[1]-1].push_back({r[0]-1, r[2]});
    }

    dist[0] = 0;
    pq.push({0, 0});
    
    while(!pq.empty()){
        int curDist = pq.top().first;
        int curNode = pq.top().second;
        pq.pop();
            
        for(auto nextPair : graph[curNode]){
            int nextNode = nextPair.first;
            int nextDist = curDist + nextPair.second;
            if(nextDist < dist[nextNode]){
                pq.push({nextDist, nextNode});
                dist[nextNode] = nextDist;
            }
        }

    }
    
    for(int i=0; i<N; i++){
        if(dist[i] <= K) answer++;
    }

    return answer;
}