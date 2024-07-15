#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <map>

using namespace std;

vector<string> split(const string& str, char delimiter) 
{
    vector<string> ret;
    string token;
    stringstream ss(str);
    while (getline(ss, token, delimiter)){
        ret.push_back(token);
    }
    return ret;
}

vector<string> solution(vector<string> record) {
    vector<string> answer;
    map<string, string> uidNickMap;
    vector<pair<string, bool> > data;
    // 레코드 파싱하고
    // uid로 맵을만들어서 가장 최근 닉네임을 맵이 들고잇어야겟네 파싱하면서
    for(string r : record){
        vector<string> str = split(r, ' ');
        switch(str[0][0]){
            case 'E':
                uidNickMap[str[1]] = str[2];
                data.push_back({str[1], true});
                break;
            case 'L':
                data.push_back({str[1], false});
                break;
            case 'C':
                uidNickMap[str[1]] = str[2];
                break;
        }
    }
    
    // 그리고 다시 반복문돌면서 최종 문자열 만들기
    for(auto i : data){
        answer.push_back(uidNickMap[i.first] + "님이 " + (i.second ? "들어왔습니다." : "나갔습니다."));
    }
    return answer;
}