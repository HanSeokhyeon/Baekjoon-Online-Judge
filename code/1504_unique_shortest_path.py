"""
1504 특정한 최단경로

1에서 n까지 이동하는데 특정한 두 정점을 지나가야한다.
최단경로의 길이를 출력하고 없으면 -1

알고리즘: 다익스트라

특정한 두 정점 a, b라하면
최단거리 = min(1-a 최단거리 + a-b 최단거리 + b-n 최단거리, 1-b 최단거리 + b-a 최단거리 + a-n 최단거리)
"""

import heapq
import sys
read = sys.stdin.readline

n, e = map(int, read().split())
graph = {i:[] for i in range(1, n+1)}
for _ in range(e):
    a, b, c = map(int, read().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, read().split())


def dijkstra(start, end):
    hq = []
    heapq.heappush(hq, (0, start))
    ds = [sys.maxsize] * (n+1)
    ds[start] = 0

    while hq:
        d, u = heapq.heappop(hq)

        for v, w in graph[u]:
            if ds[u] < d:
                continue

            if ds[v] > ds[u] + w:
                ds[v] = ds[u] + w
                heapq.heappush(hq, (ds[v], v))

    return ds[end]


common = dijkstra(v1, v2)
case1, case2 = dijkstra(1, v1) + common + dijkstra(v2, n), dijkstra(1, v2) + common + dijkstra(v1, n)
result = min(case1, case2)
if result >= sys.maxsize:
    result = -1
print(result)
