#include <string>
#include <algorithm>
#include <vector>

using namespace std;
int parent[100];
int cost[100]; 
bool cmp(vector<int> a, vector<int> b) {
    return a[2] < b[2];
}

int find(int node){
    if(parent[node] == node) return node;
    return parent[node] = find(parent[node]);
}

int solution(int n, vector<vector<int>> costs) {
    int answer = 0;
    for(int i=0; i<n; i++){
        parent[i] = i;
    }
    sort(costs.begin(), costs.end(), cmp); 
    
    for(vector<int>costVector : costs){
        int a = find(costVector[0]);
        int b = find(costVector[1]);
        int v = costVector[2];
        
        if( a != b){
            answer += v;
            parent[a] = b;
        }
    }
    return answer;
}