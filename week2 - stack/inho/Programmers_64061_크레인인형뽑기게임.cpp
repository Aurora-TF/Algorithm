#include <string>
#include <vector>
#include <stack>

using namespace std;

int solution(vector<vector<int>> board, vector<int> moves) {
    int answer = 0;
    int n = board.size();
    stack<int> bucket;
    vector<stack<int> > stackBoard(n);
    
    for(int i=n-1; i>=0; i--){
        for(int j=0; j<n; j++){
            if(board[i][j] != 0)
                stackBoard[j].push(board[i][j]);
        }
    }
    
    for(int i=0; i<moves.size(); i++){
        int move = moves[i]-1;
        if(stackBoard[move].empty()) continue;
        int doll = stackBoard[move].top();
        stackBoard[move].pop();
        
        if(!bucket.empty() && bucket.top() == doll){
            bucket.pop();
            answer+=2;
        }else{
            bucket.push(doll);
        }
    }
    
    return answer;
}