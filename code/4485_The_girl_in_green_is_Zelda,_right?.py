"""
4485 녹색 옷을 입은 애가 젤다지?

링크가 0, 0에서 n-1, n-1까지 이동한다.
지나가는 곳의 값은 모두 더해진다.
최솟값은?

알고리즘: 다익스트라

1. dfs를 0, 0에서부터 돌린다.
2. check 배열을 만들어서 그 지점까지 든 비용을 기록한다.
3. 새로운 곳으로 갈 때 현재 + 다음 비용 vs 다음 지역에 check 배열을 확인해 비교한다.
4. check[n-1][n-1] 출력
"""

import sys
read = sys.stdin.readline


def dfs():
    stack = [(0, 0)]
    check = [[sys.maxsize]*n for _ in range(n)]
    check[0][0] = area[0][0]
    dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while stack:
        x, y = stack.pop()

        for dx, dy in dxy:
            nx, ny = x+dx, y+dy
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            nxt = check[x][y] + area[nx][ny]
            if nxt < check[nx][ny]:
                check[nx][ny] = nxt
                stack.append((nx, ny))

    return check[-1][-1]


def bfs():
    q = [(0, 0)]
    check = [[sys.maxsize] * n for _ in range(n)]
    check[0][0] = area[0][0]
    dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while q:
        new_q = []
        for x, y in q:

            for dx, dy in dxy:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < n and 0 <= ny < n):
                    continue
                nxt = check[x][y] + area[nx][ny]
                if nxt < check[nx][ny]:
                    check[nx][ny] = nxt
                    new_q.append((nx, ny))

        q = new_q

    return check[-1][-1]


n = int(read())
i = 1
while n:
    area = [list(map(int, read().split())) for _ in range(n)]
    print("Problem {}: {}".format(i, bfs()))
    i += 1

    n = int(read())
