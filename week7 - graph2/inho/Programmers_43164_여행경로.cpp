#include <string>
#include <vector>
#include <set>
#include <iostream>
#include <unordered_map>

using namespace std;

unordered_map<string, int> str2idx;
unordered_map<int, string> idx2str;
vector<vector<int>> visit;
bool found = false;
vector<string> answer;

void dfs(int node, vector<string> path, int cnt){
    if(path.size() == cnt) {
        found = true;
        answer = path;
        return;
    }
    
    for(int i=0; i<visit.size(); i++){
        if(visit[node][i] == 0) continue;
        visit[node][i]--;
        path.push_back(idx2str[i]);
        dfs(i, path, cnt);
        if(found) return;
        visit[node][i]++;
        path.pop_back();
    }
}

vector<string> solution(vector<vector<string>> tickets) {
    set<string> s;

    for(auto tmp : tickets){
        s.insert(tmp[0]);
        s.insert(tmp[1]);
    }
    
    int i = 0;
    for(string tmp: s){
        str2idx[tmp] = i;
        idx2str[i++] = tmp;
    }
    
    visit = vector<vector<int>>(i, vector<int>(i, 0));
    
    int cnt = 1;
    for(auto tmp : tickets){
        int idx1 = str2idx[tmp[0]];
        int idx2 = str2idx[tmp[1]];
        
        visit[idx1][idx2]++;
        cnt++;
    }
    
    vector<string> path;
    path.push_back("ICN");
    
    dfs(str2idx["ICN"], path, cnt);
    
    return answer;
}