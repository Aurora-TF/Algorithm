#include <string>
#include <vector>
#include <map>
using namespace std;
map<string, int> cntMap;
int complete();

int solution(vector<string> want, vector<int> number, vector<string> discount) {
    int answer = 0;
    
    for(int i=0; i<want.size(); i++){
        cntMap[want[i]] = number[i];
    }
    
    for(int i=0; i<10; i++){
        cntMap[discount[i]]--;
    }
    
    for(int i=0; i<discount.size() - 10; i++){
        answer += complete();
        cntMap[discount[i]]++;
        cntMap[discount[i+10]]--;
    }
    
    return answer;
}

int complete(){
    for(auto i = cntMap.begin(); i!=cntMap.end(); i++){
        if(i->second != 0){
            return 0;
        }
    }
    return 1;
}