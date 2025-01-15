#include <iostream>
#include <vector>
#include <math.h>
using namespace std;

// 이것도 지난번 삼각형이랑 비슷한 방식으로 풀수일ㅆ을지도

// 1번째 행부터
// 나랑 같은열 제외 나머지중 제일 큰값을 나랑 더하기

int solution(vector<vector<int> > land)
{
    int answer = 0;

    for(int i=1; i<land.size(); i++)
    {
        for(int j=0; j<4; j++)
        {
            land[i][j] += max(max(land[i-1][(j+1)%4], land[i-1][(j+2)%4]), land[i-1][(j+3)%4]);
            if(i == land.size()-1) answer = land[i][j] > answer ? land[i][j] : answer;
        }
        
    }

    return answer;
}
