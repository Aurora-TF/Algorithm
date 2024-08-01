# 인접 행렬과 인접 리스트
1. 인접 행렬은 O(N^2)의 공간을 필요로 하지만, 검색에 O(1)시간이 들고 구현이 간단하다.
2. 단, 인접 행렬은 sparse 행렬(희소 행렬)이므로 빈 공간이 많아 메모리 낭비가 크다.
3. 인접 리스트는 O(N^2)의 공간을 필요로 하지만, 빈 공간이 없어 메모리 효율이 좋다.
4. 검색에 O(N)이 걸릴 수 있고, 구현이 조금 더 까다롭다.

## 그래프 탐색
1. DFS: 더 이상 탐색할 노드가 없을 때까지 일단 가본다. 그러다가 더 이상 탐색할 노드가 없으면 최근에 방문했던 노드로 되돌아간 다음 가지 않은 노드를 방문한다. 
2. BFS: 현재 위치에서 가장 가까운 노드부터 모두 방문하고 다음 노드로 넘어간다. 그 노드에서 또 다시 가장 가까운 노드부터 모두 방문한다. 

### DFS
`stack`과 `재귀` 두 가지 버전이 존재한다.

- stack
1. stack에 시작 노드를 넣는다.
2. stack에서 노드 하나를 꺼내어, 방문했는 지 확인한다. 방문했다면 다음 stack을 팝하고, 방문 안했다면 방문 처리를 해준다음 넘어간다. **중요한 것은 stack에 넣을 때 방문처리를 하는 것이 아니라, stack에서 꺼낼 때 방문 처리를 한다.**
3. 방문한 노드와 인접한 모든 노드를 stack에 넣고, 1을 반복한다. 
4. stack이 비어있다면 종료한다.

- 재귀함수
dfs(n): n번 노드를 방문 처리하고, n번 노드와 인접한 노드 중 아직 방문하지 않은 노드를 탐색
1. dfs(start)로 시작하여 start 노드를 방문처리 
2. start 노드에 연결된 노드 중 하나를 dfs(next)로 방문
3. 방문한 노드는 가지않는다.

재밌는 차이는 stack의 경우 방문했는 지 안했는 지 처리를 stack에서 꺼낼 때 한다.
```py
def dfs_stack(n, start, graph):
    visited = [False for _ in range(n + 1)]
    stack = [start]
    
    while stack:
        cur = stack.pop()
        if visited[cur]:
            continue
        
        print(cur, end=" ")
        visited[cur] = True
        
        for node in graph[cur]:
            stack.append(node)
```

반면에 재귀의 경우는 재귀 함수를 실행할 때 넣는다.
```py
def dfs_recursive(n, cur, visited, graph):
    visited[cur] = True
    print(cur, end=" ")
    for node in graph[cur]:
        if visited[node]:
            continue
        dfs_recursive(n, node, visited, graph)
```

이 두 함수의 `visited` 위치 차이를 보도록 하자. 왜 이런 차이가 나오냐면 stack의 경우 방문할 '후보'를 넣는 것이다. 즉, 당장에 next로 방문할 것을 넣는게 아니라, '후보'를 넣기 때문에 방문했다는 표시를 달지 않는다. 반면에 재귀함수를 다음으로 방문할 값을 재귀함수로 바로 실행하는 개념이다. 따라서, `visited` 검사를 재귀함수 실행 직전에 하는 것이다.

### BFS
시작 노드를 queue에 넣고 방문 처리를 해준다.

1. queue에서 node를 pop한다.
2. node에 인접한 모든 node들 중 방문하지 않은 node를 queue에 넣고, 방문 처리한다.
3. queue가 빌 때까지 반복한다.

재밌는 것은 stack기반의 dfs를 사용할 때는, 방문 했는 지 안했는 지를 stack에서 pop할 때 했지만, bfs는 queue에 넣기 전에 방문 했는 지를 검사한다. 이러한 이유는 bfs는 바로 다음에 방문할 node를 queue에 넣는 것이고, stack기반 dfs는 다음에 방문할 node가 아니라 미래에 방문할 가능성이 있는 후보를 넣기 때문이다. 따라서, 바로 방문하지 않으니 방문 처리를 해주지 않는 것이다.

```py
def bfs(n, start, graph):
    visited = [False for _ in range(n+1)]
    q = deque()
    q.append(start)
    visited[start] = True
    
    while q:
        cur = q.popleft()
        print(cur, end=" ")
        for node in graph[cur]:
            if visited[node]:
                continue
            visited[node] = True
            q.append(node)
```

### DFS와 BFS의 차이
1. DFS는 깊이 찔러 들어가는 동작
2. BFS는 가중치가 같다는 가정하에 최단 경로를 보장

따라서, 최적의 해를 뽑는 경우의 수 문제는 DFS가 많이 나오고, 최단 경로 문제는 BFS가 많이 나온다.

## 다익스트라
BFS에서 간선의 가중치가 모두 같다는 가정 하에서 최단 경로를 보장한다는 말은 사실, 간선의 가중치가 모두 같다면 간선의 갯수가 최하로 나오는게 최단 경로이기 때문이다. 그러나, 간선에 가중치가 다른 경우는 다르다. 이 경우는 간선의 갯수를 최하로 가는 경로가 최단 경로가 아니라, 그냥 가중치 값이 작은게 최단 경로이다. 