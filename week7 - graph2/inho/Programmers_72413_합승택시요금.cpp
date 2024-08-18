#include <string>
#include <vector>

using namespace std;

// 플로이드와샬해서
// 노드들 돌면서 dist의 a, b, s 합이 제일 작은 노드 구하면 되는듯?

#define INF 10000000
int solution(int n, int s, int a, int b, vector<vector<int>> fares) {
    vector<vector<int>> adj(n, vector<int>(n, INF));
    int answer = 0;
    
    for(auto e: fares){
        adj[e[0]-1][e[1]-1] = e[2];
        adj[e[1]-1][e[0]-1] = e[2];
    }
    for(int i=0; i<n; i++){
        adj[i][i] = 0;
    }
    
    for(int k = 0; k < n; k++)
        for(int i = 0; i < n; i++) 
            for(int j = 0; j < n; j++) 
                if (adj[i][k] + adj[k][j] < adj[i][j])  
                    adj[i][j] = adj[i][k] + adj[k][j];
    
    
    int min = INF; s--;a--;b--;
    for(int i=0; i<n; i++){
        int sum = adj[i][s] + adj[i][a] + adj[i][b];
        min = sum < min ? sum : min;
    }
    
    
    return min;
}