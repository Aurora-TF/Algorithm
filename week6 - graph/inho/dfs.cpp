#include <string>
#include <vector>

using namespace std;

bool visit[20];
int cnt;
vector<int> num;

void dfs(int index, int sum, int target){
    if(index == num.size()){
        if(sum == target) cnt++;
        return;
    } 
    
    dfs(index+1, sum + num[index], target);
    dfs(index+1, sum - num[index], target);
}

int solution(vector<int> numbers, int target) {
    num = numbers;
    
    dfs(0, 0, target);
    return cnt;
}
