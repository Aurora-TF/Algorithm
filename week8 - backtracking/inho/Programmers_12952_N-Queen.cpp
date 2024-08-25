#include <string>
#include <vector>
using namespace std;

int answer;
vector<int> board;
int n;
bool check(int address, int cnt) {
    for (int i=0; i<cnt; i++) {
        if (board[i] == address) return false;
        if (abs(board[i]-address) == abs(cnt-i)) return false;
    }
    return true;
}

void dfs(int cnt) {
    if (cnt == n) {
        answer++;
        return;
    }
    for (int i=0; i<n; i++) {
        if (check(i, cnt)) {
            board[cnt] = i;
            dfs(cnt+1);
        }
    }
}

int solution(int N) {
    n = N;
    board = vector<int>(n, 0);
    dfs(0);
    return answer;
}