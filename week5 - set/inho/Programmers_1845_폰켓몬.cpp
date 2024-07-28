#include <vector>
#include <set>
using namespace std;

int solution(vector<int> nums)
{
    int answer = 0;
    int r = nums.size() / 2;
    set<int> monsterSet;
    
    for(int i : nums)
    {
        monsterSet.insert(i);
    }
    int n = monsterSet.size();
    
    return r < n ? r : n;
}