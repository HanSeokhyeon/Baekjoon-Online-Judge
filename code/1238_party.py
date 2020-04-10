"""
1238 파티

N개의 마을에 N명의 학생이 살고 있다.
마을에는 M개의 도로가 있다.
도로마다 지나는데 걸리는 시간이 다르다.;
학생들이 파티를 참석하기 위해 걸어갔다가 돌아와야한다.
돌아오는 길은 다를 수 있다.
가장 오래 걸리는 사람은?

알고리즘: 다익스트라

1. n마을에서 모든 정점에 대해 최단거리를 구한다. (다익스트라)
2. n명의 학생 반복
    1. 학생 위치에서 파티까지의 최단거리를 구한다.
    2. 기존에 구해 놓은 돌아오는 길에 거리와 합해 최대를 비교한다.
3. 출력
"""
import heapq
import sys
read = sys.stdin.readline

n, m, x = map(int, read().split())
graph = {i:[] for i in range(1, n+1)}
for i in range(m):
    u, v, w = map(int, read().split())
    graph[u].append((v, w))


def dijkstra(start):
    hq = []
    heapq.heappush(hq, (0, start))
    ds = [sys.maxsize]*(n+1)
    ds[start] = 0
    while hq:
        d, idx = heapq.heappop(hq)
        if ds[idx] < d:
            continue

        for v_, w_ in graph[idx]:
            if ds[v_] > d + w_:
                ds[v_] = d + w_
                heapq.heappush(hq, (ds[v_], v_))

    return ds

max_distance = 0
x_ds = dijkstra(x)
for i in range(1, n+1):
    n_ds = dijkstra(i)
    distance = n_ds[x] + x_ds[i]
    max_distance = max(max_distance, distance)

print(max_distance)
