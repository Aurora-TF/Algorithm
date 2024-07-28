#include <string>
#include <vector>
#include <iostream>
#include <set>

using namespace std;

vector<int> solution(int n, vector<string> words) {
    vector<int> answer = {0 , 0};
    set<string> wordSet;
    string prevWord = "";
    for(int i=0; i<words.size(); i++){
        int teller = i % n;
        int turn = i / n;
        string word = words[i];
        if((prevWord != "" and prevWord[prevWord.size()-1] != word[0]) or wordSet.find(word) != wordSet.end()){
            answer[0] = teller+1;
            answer[1] = turn+1;
            break;
        }
        wordSet.insert(word);
        prevWord = word;
    }
    
    return answer;
}