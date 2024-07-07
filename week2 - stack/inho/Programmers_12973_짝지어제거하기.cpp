#include <iostream>
#include<string>
#include<stack>
using namespace std;

int solution(string s)
{
    stack<char> st;
    for(int i=0; i<s.length(); i++){
        char tmp = s[i];
        
        if(!st.empty() && st.top() == tmp){
            st.pop();
        }else{
            st.push(tmp);
        }
    }

    return st.empty() ? 1 : 0;
}