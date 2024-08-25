# Week8 - backtracking

## 1. 피로도 (programmers 87946)

바보 같이 다 풀어 놓고 마지막에 방문하지 않은 던전을 세서 시간 쓴 문제 입니다.
dfs를 활용한 backtracking 으로 풀 수 있습니다.

## 2. N-Queen (programmers 12952)

간만에 보는 N-Queen 문제 였습니다.  
잘 기억이 안나서 애를 좀 먹었는데 결국 1차원 리스트의 값이 col이 되게 하면 되는 문제 였습니다.  
대각선도 계산해주어야 합니다.

이후 row가 끝까지 진행 되었을 때 return 1을 해주어 완료된 경우의 수를 하나 늘려줍니다.

## 3. 양궁대회 (programmers 92342)

dfs를 활용한 backtracking 으로 풀었습니다.  
반복문을 통해 화살을 쏘는 모든 경우의 수를 계산했고, 모든 화살을 다 사용했을때 비교를 통해 재귀 탈출 조건을 만족 시켰습니다.

## 4. 외벽 점검 (programmers 60062)

완전 탐색이 필요한 문제였으나 역시 어려웠습니다.  
우선 시계, 반시계 방향 모두 탐색이 가능하나 굳이 돌아올 일은 없고 한 방향으로만 진행한다 가정할 수 있습니다. 또한 어느 지점에서 출발해도 문제 해결이 가능하도록 기존 weak 리스트가 한 줄로 있는 형태처럼 구성 해줍니다.

```py
for i in range(weak_length):
    weak.append(weak[i] + n)
```

이후 `친구의 수 + 1`을 answer로 설정해서 모든 친구가 도전해도 실패하는 경우를 설정해둡니다.  
반복문을 weak의 길이 만큼 수행합니다. 이는 start를 모든 지점에서 수행할 수 있도록 하기 위함입니다.  
후보는 permutation을 통해 조합합니다. 순서를 따지기 때문에 permutation을 썼습니다.

후보 list를 반복문 돌립니다. 시작점에서 해당 후보가 커버할 수 있는 거리까지 더한 값을 `확인 가능 거리 (possible_check_length)`로 설정 해둔 뒤, 특정 지점까지 도달 할 수 있는 경우에는 계속 진행, 그렇지 못할 경우 다음 후보로 넘어간 뒤 `확인 가능 거리 (possible_check_length)`를 업데이트 해줍니다.  
한 번의 후보 list 반복문을 돌렸을 때 결과를 answer에 저장해줍니다. 이후 반복합니다.