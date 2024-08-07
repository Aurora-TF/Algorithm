## 1. Union-Find 구현
1. union-find는 상호베타적 집합으로, 집합 안에 중복이 되는 원소가 없고 순서가 무의미하며, 다른 집합과 교집합을 가지지 않는다.
2. union-find는 상호베타적 집합이므로 다른 집합과 교집합이 없어 사이클이 생기지 않는다.
3. union-find는 disjoint set으로 만드는데, 이 때 배열을 사용한다.
4. 배열의 인덱스는 node의 번호이고, 값은 해당 node의 부모 node이다. 즉 node 3의 부모가 2라면 disjointset[3] = 2이다. 참고로 초기화 할 때는 인덱스와 값을 똑같이 설정해준다.
5. root 노드는 부모 노드가 없기 때문에 자기 자신이다. 가령 root node가 2라면 disjointset[2] = 2이다.
6. 따라서, 배열의 크기는 원소의 가장 큰 값이 된다. 
7. disjointset 배열 하나에 여러 트리들이 있을 수 있다. 이들은 서로 부모가 다르므로 서로 배타적이다. 따라서, 집합의 갯수가 몇 개냐고 한다면 인덱스와 값이 같은 node의 갯수를 구하면 된다.
8. 집합 알고리즘은 집합끼리 합치는(union) 연산과 탐색하는 연산(find)가 주된 알고리즘이다. 그래서 union-find이다.
9. find: 두 원소가 같은 집합에 있는 지 확인하는 연산으로, 두 노드의 root 노드 값이 동일하면 같은 집합, 아니면 다른 집합니다.
10. 이때, find연산 한 번마다 O(N)시간이 걸리는데, 이 find 탐색을 줄이기 위해서 처음부터 disjointset의 값을 부모 노드를 쓰는 것이 아니라, root 노드로 쓰도록 하여 O(1)안에 해결할 수 있다.
11. union: 합치기 연산은 두 집합의 root node 중에 아무거나 골라서 한쪽의 root node값을 다른 집합의 root node로 바꾸면 된다.
12. 가령 첫번째 집합의 root node가 2이고, 두번째 집합의 root node가 3일 때, root node 2아래로 root node 3이 들어간다면 disjointset[3] = 2로 바꿔주면 된다.
13. 문제는 이렇게 union을 하다보면 tree의 깊이가 길어 질 수 있다. 따라서 rank 기반의 union을 해야한다.
14. rank 기반의 union은 leaf에서 root까지의 거리 중 가장 먼 rank가 해당 집합을 나타내는 rank이며, rank가 작은 집합이 큰 집합 아래로 합쳐져야 트리의 균형이 이루어진다.

## 2. 폰켓몬
그저 set...

## 3. 영어 끝말잇기
그저 구현

## 4. 전화번호 목록
정렬 후에 각 전화번호 접두사 확인

## 5. 섬연결하기
프림? 크루스칼? 알고리즘이었나 기억이 가물가물 가물치했지만 어찌됐거나 union-find로 사이클 검사해서 최소 간선만 이어주도록 했습니다.