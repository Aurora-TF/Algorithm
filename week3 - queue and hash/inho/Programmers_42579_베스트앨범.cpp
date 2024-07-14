#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <algorithm>

using namespace std;
map<string, int> genreCnt;

bool cmp(pair<int, int> a, pair<int, int> b){
    if(a.second > b.second){
        return true;
    }else if (a.second == b.second){
        if(a.first < b.first) return true;
        else return false;
    }else{
        return false;
    }
}

bool cmp2(pair<string, pair<int, int> > a, pair<string, pair<int, int> > b){
    if(genreCnt[a.first] > genreCnt[b.first])
        return true;
    return false;
}

vector<int> solution(vector<string> genres, vector<int> plays) {
    vector<int> answer;
    map<string, vector<pair<int, int> > > album;
    vector<pair<string, pair<int,int> > > lastv; // genre, i
    
    for(int i=0; i<genres.size(); i++){
        album[genres[i]].push_back({i, plays[i]});
        genreCnt[genres[i]] += plays[i];
    }
    
    for(auto i = album.begin(); i != album.end(); i++){
        sort(i->second.begin(), i->second.end(), cmp);
        lastv.push_back({i->first, {i->second[0].first, i->second.size() == 1 ? -1 : i->second[1].first}});
    }

    sort(lastv.begin(), lastv.end(), cmp2);
    
    for(auto i = lastv.begin(); i!= lastv.end(); i++){
        answer.push_back(i->second.first);
        if(i->second.second != -1)
            answer.push_back(i->second.second);
    }
    
    return answer;
}