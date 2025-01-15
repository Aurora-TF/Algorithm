#include <string>
#include <vector>
#include <iostream>
#include <math.h>

using namespace std;

// 두번째 줄부터 나한테 올수있는 이전 경로들중 값이 큰거로 더해주기
// 10, 15
// 18, 16, 15
// 20, 25, 20, 19
// 24, 30, 27, 26, 24

// 더할때마다 그냥 MAX값 확인하면 되겠네
// 10000 * 500 = 5000000 -> INT로 해도됨

// i, j 중에서
// i-1, j-1
// i -1, j 그대로

int solution(vector<vector<int>> triangle) 
{
    int answer = 0;
    
    for(int i=1; i<triangle.size(); i++)
    {
        for(int j = 0; j<=i; j++)
        {
            int tmp = 0;

            if(j-1 >= 0)
            {
                tmp = triangle[i-1][j-1];
            }
            
            if(j != i)
            {
                tmp = max(tmp, triangle[i-1][j]);
            }
            
            triangle[i][j] += tmp;
            answer = max(answer, triangle[i][j]);
        }
    }
    
    return answer;
}