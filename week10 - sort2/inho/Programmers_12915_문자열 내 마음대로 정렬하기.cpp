#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int n = 0;
bool cmp(const string a, const string b){
    if(a[n] < b[n]) return true;
    if(a[n] == b[n]) return a < b;
    return false;
}

vector<string> solution(vector<string> strings, int N) {
    n = N;
    sort(strings.begin(), strings.end(), cmp);
    
    return strings;
}