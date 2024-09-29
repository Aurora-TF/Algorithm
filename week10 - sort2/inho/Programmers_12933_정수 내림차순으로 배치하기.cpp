#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

long long solution(long long n) {
    long long answer = 0;
    vector<int> vec;
    while(n > 0){
        int tmp  = n % 10;
        vec.push_back(tmp);
        n /= 10;
    }
    sort(vec.begin(), vec.end());
    long long dec = 1;
    for(int a : vec){
        answer += dec * a;
        dec *= 10;
    }
    return answer;
}