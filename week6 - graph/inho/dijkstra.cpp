#include <vector>
#include <queue>
#include <iostream>

using namespace std;

# define INF 99999999

vector<int> dijkstra(int start, int n, vector<pair<int, int>> graph[])
{
    vector<int> dist(n, INF);
    priority_queue<pair<int, int>> pq;

    dist[start] = 0;
    pq.push({ 0, start });

    while (!pq.empty())
    {
        int curDist = -pq.top().first;
        int curNode = pq.top().second;
        pq.pop();

        for (int i = 0; i < graph[curNode].size(); i++)
        {
            int nextDist = curDist + graph[curNode][i].first;
            int nextNode = graph[curNode][i].second;

            if (nextDist < dist[nextNode])
            {
                dist[nextNode] = nextDist;
                pq.push({ -nextDist, nextNode });
            }
        }
    }

    return dist;
}

int main()
{
    const int n = 10;
    int e = 20;
    vector<pair<int, int>> graph[n];

    for (int i = 0; i < e; i++)
    {
        int from, to, cost;
        cin >> from >> to >> cost;
        graph[from].push_back({ cost, to });
        graph[to].push_back({ cost, from });
    }

    vector<int> dist = dijkstra(0, n, graph);
    
    cout << dist[n - 1] << endl;
    
    return 0;
}