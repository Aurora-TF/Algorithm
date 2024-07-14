#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>
#include <sstream>
#include <algorithm>
using namespace std;

vector<int> solution(vector<string> id_list, vector<string> report, int k) {
    vector<int> answer;
    unordered_map<string, int> banned;
    unordered_map<string, vector<string> > userMap;
    
    for(string r: report){
        stringstream ss(r);
        string banner, bannee;
        getline(ss, banner, ' ');
        getline(ss, bannee, ' ');

        vector<string> bannees = userMap[banner];
        if(find(bannees.begin(), bannees.end(), bannee) != bannees.end()) continue;
        userMap[banner].push_back(bannee);
        banned[bannee]++;
    }
    
    for(string banner : id_list){
        int cnt = 0;
        vector<string> bannees = userMap[banner];
        for(string bannee : bannees){
            if (banned[bannee] >= k) cnt++;
        }
        answer.push_back(cnt);
    }
    
    return answer;
}