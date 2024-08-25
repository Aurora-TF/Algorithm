#include <string>
#include <vector>

using namespace std;

// 처음엔 점수 낮은거부터 찾으려했음.
// 문제 조건이 까다로워서 제대로 읽고 이해했어야했음

// 참고한 해답에서는 높은 점수구간부터 탐색
// 사실상 높은구간에서 최솟값으로 이긴담에 점수차를 벌리기 위해 가장 높은곳에 남은 화살도 다 쏟는 선택
// 그리고 어차피 가장 낮은 점수구간까지는 알아서 돈다.
// 어피치를 이기지도 못하는데 중간중간 점수를 흩뿌리는게 불필요!
// 근데 실제로 이 아이디어를 떠올릴 수 있을까? 가 미지수

// 어피치 이길 수 있으면 이길만큼 쏟아붓거나
// 남은거 다 쏟아붓거나 
// 이 두개 생각하는게 키가 아니였을까

// 두 점수차의 max 인 것도 있음.

// 키 아이디어도 어려운데 눈에 안띄지만 중요한 조건도 있어서 많이 어려운문제..
// 프로그래머스는 당장 이문제를 lev3으로 올려랏

vector<int> apeach;
vector<int> lion;
vector<int> answer = {-1};
int maxValue = 0;
int n;

void dfs(int idx, int restCnt){
    if(restCnt == 0){
        int diff = 0;

        for(int i=0; i<11; i++){
            if (lion[i]>apeach[i]) diff += (10 - i);
            else if (apeach[i]) diff -= (10 - i);
        }

        if(maxValue < diff){
            maxValue = diff;
            answer = lion; // 깊은복사임 ㄱㅊ
        }else if(maxValue == diff){
            for(int i=10; i>=0; i--){
                if(answer[i] < lion[i]){
                    answer = lion;
                }else if(answer[i] > lion[i]){
                    break;
                }
            }
        }
        return;
    }

    for(int i=idx; i<=10; i++)
    {
        int num = apeach[i]+1;
        if (num > restCnt) num = restCnt;
        lion[i] = num;
        dfs(idx + 1, restCnt-num);
        lion[i] = 0;
    }
}

vector<int> solution(int N, vector<int> info) {
    n = N;
    apeach = info;
    lion = vector<int>(11, 0);
    dfs(0, n);
    
    return answer;
}