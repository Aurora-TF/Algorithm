#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <algorithm>

using namespace std;

vector<int> solution(string s) {
    vector<int> answer;
    bool visit[100001] = {false};
    
    stringstream ss(s.substr(1,s.length()-2));
    vector<std::vector<int>> parsedArray(501);
    string temp;

    while (getline(ss, temp, '{')) {
        string inner;
        if (getline(ss, inner, '}')) {
            stringstream innerStream(inner);
            string number;
            vector<int> row;

            while (getline(innerStream, number, ',')) {
                row.push_back(stoi(number));
            }
            sort(row.begin(), row.end());
            parsedArray[row.size() -1] = row;
        }
    }
    
    for(auto a : parsedArray)
    {
        if(a.size() == 0) break;
        for(auto b : a)
        {
            if(!visit[b-1])
            {
                visit[b-1] = true;
                answer.push_back(b);
            }
        }
    }
    
    return answer;
}