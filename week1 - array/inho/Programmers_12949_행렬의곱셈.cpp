#include <string>
#include <vector>

using namespace std;

vector<vector<int>> solution(vector<vector<int>> arr1, vector<vector<int>> arr2) {
    vector<vector<int>> answer;
    int row1 = arr1.size();
    int col1 = arr1[0].size();
    
    int row2 = arr2.size();
    int col2 = arr2[0].size();
    
    for(int i=0; i<row1; i++){
        vector<int> tmp;
        for(int j=0; j<col2; j++){
            int value = 0;
            for(int k=0; k<row2; k++){
                value += arr1[i][k] * arr2[k][j];
            }
            tmp.push_back(value);
        }
        answer.push_back(tmp);
    }
    return answer;
}