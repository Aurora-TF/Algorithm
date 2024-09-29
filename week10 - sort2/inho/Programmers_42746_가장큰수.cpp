#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

bool cmp2(const string &a, const string &b){
    return a+b > b+a;
}

bool cmp(int numA, int numB){
    string a = to_string(numA);
    string b = to_string(numB);
    int aLen = a.size();
    int bLen = b.size();
    int n = aLen > bLen ? bLen : aLen;
    for(int i=0; i<n; i++){
        if(a[i] > b[i]){
            // cout << "1." << a << ">" << b << endl;
            return true;
        }
    }
    // 여까지 왔으면 a가 무조건 더 긴건데
    if(a[n] > b[n-1]){
        // cout << "2." << a << ">" << b << endl;
        return true;
    }
    // cout << "3." << a << "<" << b << endl;
    
    return false;
    
}

string solution(vector<int> numbers) {
    string answer = "";
    vector<string> stringNumbers;
    for(int i : numbers){
        stringNumbers.push_back(to_string(i));
    }
    sort(stringNumbers.begin(), stringNumbers.end(), cmp2);
    for(string a : stringNumbers){
        // cout << a << " " << endl;
        answer.append(a);
    }
    
    return answer[0] == '0' ? "0" : answer;
}