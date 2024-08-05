#include <vector.h>

#define MAX_NODE_CNT 6

vector<pair<int, int> > edges;
edges.push_back({0, 1});
edges.push_back({1, 4});
edges.push_back({1, 3});
edges.push_back({2, 5});

// 인접 배열
int adjArr[MAX_NODE_CNT][MAX_NODE_CNT];

for(auto p : edges){
    adjArr[p.first][p.second] = 1;
    adjArr[p.second][p.first] = 1; // 양방향일 경우
}

// 인접 리스트
vector<int> adjList[MAX_NODE_CNT];

for(auto p : edges){
    adjList[p.first].push_back(p.second);
    adjList[p.second].push_back(p.first); // 양방향일 경우
}

// 인접배열보다는 인접 리스트를 사용할 때, 불필요한 메모리 사용을 막을 수 있습니다.
