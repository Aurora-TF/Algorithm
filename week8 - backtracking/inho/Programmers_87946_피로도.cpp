#include <string>
#include <vector>

using namespace std;
// 던전 갯수는 8 이하
// 탐험 가능한 최대 던전 수

// 진짜 완전탐색 해야함 -> 순열처럼

// dfs 로 visit 배열 돌면서?
bool visit[8];
int maxCnt = -1;
int N;
vector<vector<int>> dun;
void dfs(int node, int stemina, int cnt){
    if(cnt == N) return; // 완성
    if(dun[node][0] > stemina) return;
    
    visit[node] = true;
    maxCnt = max(++cnt, maxCnt);
    
    for(int i=0; i<N; i++){
        if(visit[i]) continue;
        dfs(i, stemina-dun[node][1], cnt);
    }
    
    visit[node] = false;
}

int solution(int k, vector<vector<int>> dungeons) {
    int answer = -1;
    
    N = dungeons.size();
    dun = dungeons;
    
    for(int i=0; i<N; i++){
        dfs(i, k, 0);
    }
    
    return maxCnt;
}