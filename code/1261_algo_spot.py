"""
1261 알고스팟

0은 빈방, 1은 벽
1, 1에서 n, m까지 갈 예정이다.
벽을 최소 몇개 부수며 갈 수 있을까

알고리즘: 다익스트라

1. bfs
    1. visit 대신 다익스트라 알고리즘 처럼
        다음 지점의 부순 벽 개수 vs 현재 지점의 부순 벽 개수 + 1
"""

import sys
read = sys.stdin.readline

m, n = map(int, read().split())
area = [list(map(int, list(read().strip()))) for _ in range(n)]


def bfs():
    q = [(0, 0)]
    check = [[200]*m for _ in range(n)]
    check[0][0] = 0
    dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while q:
        new_q = []

        for x, y in q:

            for dx, dy in dxy:
                nx, ny = x+dx, y+dy
                if not (0 <= nx < n and 0 <= ny < m):
                    continue
                if area[nx][ny] == 0:
                    nxt = check[x][y]
                else:
                    nxt = check[x][y] + 1
                if nxt < check[nx][ny]:
                    check[nx][ny] = nxt
                    new_q.append((nx, ny))

        q = new_q

    return check[-1][-1]


print(bfs())
