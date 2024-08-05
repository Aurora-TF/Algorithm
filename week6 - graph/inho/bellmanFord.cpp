// edge의 cost에 음수가 있을때
// "음수 사이클"(해당 사이클을 돌면 cost가 총 음수가 되는) 있으면 다익스트라 알고리즘을 돌리면
// dist가 전부 -무한대가 됨. 음수 사이클을 뱅뱅 돌다가 가는게 더 작은 cost라고 판단하니

#include <iostream>
#include <vector>
#include <algorithm>

#define INF 214700000

using namespace std;

int V, E, K;

vector<vector<pair<int, int>>> graph;

vector<int> bellman_ford()
{
	vector<int> dist(V, INF);
	dist[K - 1] = 0;

    // 노드갯수-1 만큼 반복
	for (int i = 0; i < V - 1; i++)
	{
		for (int j = 0; j < V; j++)
		{
			for (int k = 0; k < graph[j].size(); k++)
			{
				if (graph[j][k].first + dist[j] < dist[graph[j][k].second])
				{
					dist[graph[j][k].second] = graph[j][k].first + dist[j];
				}
			}
		}
	}

	int sum = 0;
	for (int i = 0; i < dist.size(); i++) {
        sum += dist[i];
    }

    // n 번째 반복
	vector<int> copyDist(dist);

	for (int j = 0; j < V; j++)
	{
		for (int k = 0; k < graph[j].size(); k++)
		{
			if (graph[j][k].first + copyDist[j] < copyDist[graph[j][k].second])
			{
				copyDist[graph[j][k].second] = graph[j][k].first + copyDist[j];
			}
		}
	}

	int copySum = 0;
	for (int i = 0; i < copyDist.size(); i++) {
        copySum += copyDist[i];
    }

	if (sum != copySum)
	{
		// n번째 반복해보니 값이 다름 => 음수사이클 있음
	}

	return dist;
}

int main(void)
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> V >> E;
	cin >> K;
	graph.assign(V, vector<pair<int, int>>());

	while (E--)
	{
		int u, v, w;
		cin >> u >> v >> w;

		graph[u - 1].push_back({w, v - 1});
	}

	vector<int> dist = bellman_ford();

	return 0;
}