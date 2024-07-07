#include <string>
#include <vector>
#include <deque>
#include <stack>
#include <iostream>

using namespace std;
deque<char> dq;
int len;

int check(int i, string s){
    stack<char> st;
    for(int j=i; j< i+len; j++){
        int index = j % len;
        switch(s[index]){
            case ']':
                if(!st.empty() && st.top() == '[')
                    st.pop();
                else
                    return false;
                break;
            case '}':
                if(!st.empty() && st.top() == '{')
                    st.pop();
                else
                    return false;
                break;
            case ')':
                if(!st.empty() && st.top() == '(')
                    st.pop();
                else
                    return false;
                break;
            default:
                st.push(s[index]);
                break;
        }
    }
    return st.empty() ? true : false;
}

int solution(string s) {
    int answer = 0;
    len = s.length();
    for(int i=0; i<len; i++){
        dq.push_back(s[i]);
    }
    
    for(int i=0; i<len; i++){
        if(check(i, s)) answer++;
    }
    
    return answer;
}

