#include <string>
#include <memory.h>
using namespace std;

// 시작좌표를 5,5 라고 가정하고 전체를 [11][11] 로 가정
int x = 5;
int y = 5;
bool visit[11][11][4]; // 위쪽방향부터 시계방향으로
int count = 0;

int solution(string dirs) {
    memset(visit, 0, sizeof(visit));
    
    for(int i=0; i<dirs.size(); i++)
    {
        switch(dirs[i]){
            case 'U':
                if(y+1 > 10) continue;
                if(visit[x][y + 1][2] == false){
                    visit[x][y + 1][2] = true;
                    visit[x][y][0] = true;
                    count++;
                }
                y++;
                break;
            case 'D':
                if(y - 1 < 0) continue;
                if(visit[x][y - 1][0] == false){
                    visit[x][y - 1][0] = true;
                    visit[x][y][2] = true;
                    count++;
                }
                y--;
                break;
            case 'R':
                if(x + 1 > 10) continue;
                if(visit[x + 1][y][3] == false){
                    visit[x + 1][y][3] = true;
                    visit[x][y][1] = true;
                    count++;
                }
                x++;
                break;
            case 'L':
                if(x - 1 < 0) continue;
                if(visit[x - 1][y][1] == false){
                    visit[x - 1][y][1] = true;
                    visit[x][y][3] = true;
                    count++;
                }
                x--;
                break;
        }
    }
    
    return count;
}
