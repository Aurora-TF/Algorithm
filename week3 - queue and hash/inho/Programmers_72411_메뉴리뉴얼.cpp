#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <iostream>
using namespace std;

unordered_map<string,int> menu;

void dfs(int idx, string tmp, string order) {
    // 처음엔 길이 0인 tmp 부터 시작해서 order사이즈까지 모든 조합을 depth로 돌아야함.
    if (tmp.size() > order.size()) {
        return ;
    }
    menu[tmp]++;
    for (int i = idx; i < order.size(); i++) {
        dfs(i+1, tmp+order[i], order);
    }
}

// course돌면서 길이 course갯수인 메뉴중에 가장많은 수 된거 넣기. 
vector<string> solution(vector<string> orders, vector<int> course) {
    for(string order: orders){
        sort(order.begin(), order.end());
        dfs(0, "", order);
    }
    
    vector<string> answer;
    
    for(int c: course){
        int max = 0;
        // m돌면서 max값 먼저 찾고
        for(auto i : menu){
            if(i.first.size() != c) continue;
            max = i.second > max ? i.second : max;
        }
        
        // max인데 2 이상인 문자열 전부 벡터에 담기
        for(auto i : menu){
            if(i.first.size() != c) continue;
            if(i.second == max && i.second >= 2){
                answer.push_back(i.first);
            }
        }
    }
    sort(answer.begin(), answer.end());    
    return answer;
}