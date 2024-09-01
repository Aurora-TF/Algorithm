#include <string>
#include <map>
#include <vector>

using namespace std;

// 이런 문제가 나오면
// 완전탐색을 해야하는지 뭔가 꼼수가 있는지 확인해야함.
// 여기서는 미네랄 순서를 못바꾸고
// 곡괭이도 한번 들면 끝
// 완전탐색일거라는 생각이 드는거지

// 다이아 나올때는 최대한다이아를 쓰는게 좋겠지만
// 이 다이아 이후에 다음 네개가 얼마나 더 다이아일지
// 다이아 곡괭이 그렇게 다썼는데 이후에 다이아연속으로 나올수도
vector<int> picks;
vector<string> minerals;
int pickCnt;
int mineralCnt;
int minStemina = 10000000;

int arr[3][3] = {{1, 1, 1}, {5, 1, 1}, {25, 5, 1}};
map<string, int> str2idx = { {"diamond",0}, {"iron",1}, {"stone",2} };

bool havePicks(){
    for(int i=0; i<3; i++){
        if(picks[i] > 0) return true;
    }
    return false;
}

void dfs(int stemina, int idx){
    if(idx >= mineralCnt){
        minStemina = min(stemina, minStemina);
        return;
    }
    if(!havePicks()){
        minStemina = min(stemina, minStemina);
    }
    
    for(int i=0; i<3; i++){
        int spend = 0;
        if(picks[i] == 0) continue;
        picks[i]--;
        for(int j=idx; j<min(idx+5, mineralCnt); j++){
            spend += arr[i][str2idx[minerals[j]]];
        }
        dfs(stemina + spend, min(idx+5, mineralCnt));
        picks[i]++;
    }
}

int solution(vector<int> pick, vector<string> mineral) {
    picks = pick;
    minerals = mineral;
    mineralCnt = mineral.size();
    
    int answer = 0;
    dfs(0, 0);
    return minStemina;
}