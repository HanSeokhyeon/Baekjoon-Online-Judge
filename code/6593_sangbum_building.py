"""
6593 상범 빌딩

3차원 빌딩에서 탈출한다.
L: 층 R: 행 C: 열
#: 금 .: 빈곳 S: 시작점 E: 출구

알고리즘: BFS

1. 1분마다 진행하며 도착지에 도착하면 break
"""

import sys
read = sys.stdin.readline


def bfs():
    q = [start]
    visit = {start: True}
    dxyz = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]

    time = 0
    while q:
        new_q = []

        for x, y, z in q:
            if (x, y, z) == end:
                return time

            for dx, dy, dz in dxyz:
                nx, ny, nz = x+dx, y+dy, z+dz
                if not (0 <= nx < l and 0 <= ny < r and 0 <= nz < c):
                    continue
                if (nx, ny, nz) not in visit and building[nx][ny][nz] != '#':
                    new_q.append((nx, ny, nz))
                    visit[(nx, ny, nz)] = True

        q = new_q
        time += 1

    return -1


l, r, c = map(int, read().split())
while l or r or c:
    building = []
    for i in range(l):
        floor = []
        for j in range(r):
            floor.append(list(read().strip()))
            for k in range(c):
                if floor[j][k] == 'S':
                    start = (i, j, k)
                elif floor[j][k] == 'E':
                    end = (i, j, k)
        read()
        building.append(floor)

    result = bfs()
    if result != -1:
        print("Escaped in {} minute(s).".format(result))
    else:
        print("Trapped!")

    l, r, c = map(int, read().split())