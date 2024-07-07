#include <string>
#include <vector>
#include <stack>

using namespace std;

vector<int> solution(vector<int> prices) {
    vector<int> answer(prices.size());
    stack<int> stack;
    
    for(int i=0; i<prices.size(); i++){
        answer[i] = prices.size() - 1 - i;
    }
    for(int i=0; i<prices.size()-1; i++){
        while( !stack.empty() && prices[stack.top()] > prices[i] ){
            answer[stack.top()] = i - stack.top();
            stack.pop();
        }
        stack.push(i);
    }
    return answer;
}


// vector<int> solution(vector<int> prices) {
//     vector<int> answer;
    
//     for(int i=0; i<prices.size(); i++){
//         int cnt = 0;
//         for(int j=i+1; j<prices.size(); j++){
//             cnt++;
//             if(prices[i] > prices[j])
//                 break;
//         }
//         answer.push_back(cnt);
//     }
    
//     return answer;
// }