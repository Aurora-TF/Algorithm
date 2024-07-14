#include <string>
#include <vector>
#include <iostream>
#include <deque>

using namespace std;

string solution(vector<string> cards1, vector<string> cards2, vector<string> goal) {
    string answer = "";
    deque<string> q1;
    deque<string> q2;
    
    for(string card: cards1){
        q1.push_back(card);
    }
    
    for(string card: cards2){
        q2.push_back(card);
    }
    
    for(string word: goal){
        if(word == q1.front()){
            q1.pop_front();
        }else if (word == q2.front()){
            q2.pop_front();
        }else{
            return "No";
        }
    }
    
    return "Yes";
}